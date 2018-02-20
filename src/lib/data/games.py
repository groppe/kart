#!/usr/bin/python3.6
import re
from bson.objectid import ObjectId
from lib.data.mongodb import game_collection

def game_by_id(game_id):
    return game_collection.find({
        '_id': ObjectId(game_id)
    })
    
def games_for_player(player_id, page_size=25, skip=0):
    player_id_regex = re.compile('^' + player_id)
    return game_collection.aggregate([
        {
            "$match": {
                "scores": {
                    "$elemMatch": {
                        "player_id": player_id_regex
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
            "$skip": skip
        },
        {
            "$limit": page_size
        },
        {
            "$project": {
                "games": 1,
                "datetime": 1,
                "scores": {
                    "$filter": {
                        "input": '$scores',
                        "as": 'score',
                        "cond": {'$match': ['$$score.player_id', player_id_regex]}
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

def delete_game(game_id):
    return game_collection.delete_one({
        '_id': ObjectId(game_id)
    })
