#!/usr/bin/python3.6
import re
from bson.objectid import ObjectId
from lib.data.mongodb import game_collection


def all_games():
    return game_collection.find()


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
            "$project": {
                "skill_matrix": 0
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
        }
    ])


def add_game(game):
    game_collection.insert_one(game)


def get_last_x_games(count):
    return game_collection.find().sort(
        [
            (
                'datetime', -1
            )
        ]
    ).limit(count)


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


def update_game_skill_matrix(id, matrix):
    game_collection.update_one(
        {
            '_id': id
        },
        {
            '$set': {
                'skill_matrix': matrix
            }
        },
        upsert=True
    )
