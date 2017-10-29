#!/usr/bin/python2.7
import data.players as player_data
import data.games as game_data


def calculate_average(games_played, total_score):
    if games_played != 0:
        average = total_score / games_played
    else:
        average = 0.0


def average_individual():
    # instantiate the ranking board
    board = instantiate_empty_array()

    # for each player
    for player_cursor in player_data.all_players():

        # initialize totals
        games_played = 0
        total_score = 0.0

        # get their last 25 games
        for game_cursor in game_data.games_for_player(player_cursor['_id'], 25):

            score_entry = get_player_score_entry(game_cursor)

            # add game data to totals
            games_played += get_number_of_games_played(game_cursor)
            total_score += get_player_score(score_entry)

        average = calculate_average(games_played, total_score)

        # create the player's board entry
        player = create_player_entry(player_cursor, average)

        # add them to the board
        board.append(player)

    # sort by average
    board = sorted(board, key=lambda player: player['average'], reverse=True)

    return board


def instantiate_empty_array():
    return []


def get_player_score_entry(game):
    return game['scores'][0]


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
