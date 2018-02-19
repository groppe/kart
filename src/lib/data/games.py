#!/usr/bin/python3.6
from lib.data.mongodb import game_collection

def games_in_range(page_size, index):
    return game_collection.find().skip(index * page_size).limit(page_size)
    
def games_for_player(player_id, number_of_games=25):
    return game_collection.aggregate([
        {
            "$match": {
                "scores": {
                    "$elemMatch": {
                        "player_id": player_id
                    }
                }
            }
        },
        {
            "$sort": {
                "datetime": -1
            }
        },
        {
            "$limit": number_of_games
        },
        {
            "$project": {
                "games": 1,
                "scores": {
                    "$filter": {
                        "input": '$scores',
                        "as": 'score',
                        "cond": {'$eq': ['$$score.player_id', player_id]}
                    }
                }
            }
        }
    ])


def add_game(game):
    game_collection.insert_one(game)

def get_last_game():
    return game_collection.find().sort(
        [
            (
                'datetime', -1
            )
        ]
    ).limit(1)[0]

def get_last_game_for_player(player_id):
    return game_collection.find(
        {
            'scores.player_id': 'U1RCMJFA4'
        }
    ).sort(
            [
                (
                    'datetime', -1
                )
            ]
    ).limit(1)[0]
