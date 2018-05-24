#!/usr/bin/python3.6
from lib.data import games as game_data
from lib.data import players as player_data
from numpy import *
from numpy.linalg import norm
from pprint import pprint
from itertools import combinations

GAME_HISTORY_RANGE = 25


def average_individual():
    rankings = instantiate_empty_array()

    for player in player_data.all_players():
        games = game_data.games_for_player(player['_id'], GAME_HISTORY_RANGE, 0)
        score = calculate_average_score_for_player(games, player['_id'])
        player_entry = create_player_entry(player, score)
        rankings.append(player_entry)

    return sorted(rankings, key=lambda player: player['average'], reverse=True)

def skill_rank():
    all_players = player_data.all_players()
    last_game = game_data.get_last_game()
    last_matrix = last_game['skill_matrix']
    
    combs = list(combinations(range(0, all_players.count()), 2))
    combs.extend(list(zip(range(all_players.count()), range(all_players.count()))))
    
    for pair in combs:
        last_matrix[pair[0]][pair[1]] = sum(last_matrix[pair[0]][pair[1]])
        last_matrix[pair[1]][pair[0]] = sum(last_matrix[pair[1]][pair[0]])
        total = last_matrix[pair[0]][pair[1]] + last_matrix[pair[1]][pair[0]]
        if total == 0:
            continue
        last_matrix[pair[0]][pair[1]] = last_matrix[pair[0]][pair[1]] / total
        last_matrix[pair[1]][pair[0]] = last_matrix[pair[1]][pair[0]] / total
    M = mat(last_matrix)
    x = mat(ones((len(last_matrix), 1), float))
    prev_x = x.copy()

    print("Converging")
    while True:
        x = x / sum(x)
        if norm(x - prev_x) < 1e-4:
            break
        else:
            prev_x = x.copy()
        x = dot(M, x)
    print("Done converging")
        

    all_players = player_data.all_players()
    rankings = []
    for player in all_players:
        rounded = "{0:.4f}".format(x[player['index'], 0])
        player_entry = create_player_entry(player, rounded)
        rankings.append(player_entry)
    
    return sorted(rankings, key=lambda player: player['average'], reverse=True)


def update_player_history_array(p1_vs_p2_arr, p1_average, p2_average, keep=GAME_HISTORY_RANGE):
    #p1_vs_p2_arr.insert(0, p1_average)
    if p1_average > p2_average:
        p1_vs_p2_arr.insert(0, 1)
    else:
        p1_vs_p2_arr.insert(0, 0)
    p1_vs_p2_arr[:keep]
    return p1_vs_p2_arr

def update_rank_matrix_with_game(matrix, game):
    scores = game['scores']
    for score in scores:
        p1_cursor = player_data.get_player(score['player_id'])
        p1_average = float(score['average'])
        p1_id = score['player_id']

        for score2 in scores:
            p2_cursor = player_data.get_player(score2['player_id'])
            p2_average = float(score2['average'])
            p2_id = score2['player_id']

            if p1_cursor is not None and p2_cursor is not None and p1_id != p2_id:
                p1_vs_p2_arr = matrix[p1_cursor['index']][p2_cursor['index']]
                p1_vs_p2_updated = update_player_history_array(p1_vs_p2_arr, p1_average, p2_average)
                matrix[p1_cursor['index']][p2_cursor['index']] = p1_vs_p2_updated

    return matrix


def populate_skill_matrix():
    all_players = player_data.all_players()
    player_count = all_players.count()
    games = []

    # get the last 25 games for each player
    for player in player_data.all_players():
        games.extend(list(game_data.games_for_player(player['_id'], 25, 0)))

    # remove duplicate games and sort all first to last
    games = [i for n, i in enumerate(games) if i not in games[n + 1:]]
    games = sorted(games, key=lambda game: game['datetime'])

    matrix = zeros((player_count, player_count, GAME_HISTORY_RANGE), float).tolist()
    game_counter = 0
    for game in games:
        matrix = update_rank_matrix_with_game(matrix, game)
        game_counter += 1
        print(game_counter)

    last_game = game_data.get_last_game()
    game_data.update_game_skill_matrix(last_game['_id'], matrix)


def increment_skill_matrix_size():
    last_game = game_data.get_last_game()
    matrix_curr = last_game['skill_matrix']

    player_count = len(matrix_curr)
    blank_vs_history = [0.0] * GAME_HISTORY_RANGE

    for vs in matrix_curr:
        vs.append(blank_vs_history)

    new_player_row = zeros((player_count + 1, GAME_HISTORY_RANGE), float).tolist()
    matrix_curr.append(new_player_row)

    game_data.update_game_skill_matrix(last_game['_id'], matrix_curr)


def instantiate_empty_array():
    return []


def calculate_average_score_for_player(games, player_id):
    games_played = 0
    total_score = 0.0

    for game in games:
        score_entry = get_player_score_entry(game, player_id)
        games_played += get_number_of_games_played(game)
        total_score += get_player_score(score_entry)

    average = calculate_average(games_played, total_score)
    return round(average, 2)


def get_player_score_entry(game, player_id):
    return next(filter(lambda s: s['player_id'] == player_id, game['scores']))


def get_player_score(score_entry):
    return float(score_entry.get('score', 0.0))


def get_number_of_games_played(cursor):
    return int(cursor.get('games', 0))


def calculate_average(games_played, total_score):
    if games_played != 0:
        return total_score / games_played
    else:
        return 0.00


def create_player_entry(cursor, average):
    return {
        'id': get_player_id(cursor),
        'name': get_player_name(cursor),
        'character': get_player_character(cursor),
        'average': average
    }


def get_player_id(cursor):
    return cursor['_id']


def get_player_name(cursor):
    return cursor.get('name', '<Unknown>')


def get_player_character(cursor):
    return cursor.get('character', '<Unknown>')
