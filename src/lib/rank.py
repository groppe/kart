#!/usr/bin/python3.6
from lib.data import games as game_data
from lib.data import players as player_data


#
# public methods
#


def average_individual():
    rankings = instantiate_empty_array()

    for player in player_data.all_players():
        games = game_data.games_for_player(player['_id'], 25, 0)
        score = calculate_average_score_for_player(games, player['_id'])
        player_entry = create_player_entry(player, score)
        rankings.append(player_entry)

    return sorted(rankings, key=lambda player: player['average'], reverse=True)

#
# private helper methods
#


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
