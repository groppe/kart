#!/usr/bin/python2.7
from mongodb import game_collection


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
