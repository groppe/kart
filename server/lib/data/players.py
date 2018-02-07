#!/usr/bin/python2.7
from lib.data.mongodb import player_collection


def all_players():
    return player_collection.find()


def get_player(player_id):
    return player_collection.find_one({
        '_id': player_id
    })


def update_player_character(player_id, character_name):
    player_collection.update_one(
        {
            '_id': player_id
        },
        {
            '$set': {
                'character': character_name
            }
        },
        upsert=True
    )


def update_player_name(player_id, new_name):
    player_collection.update_one(
        {
            '_id': player_id
        },
        {
            '$set': {
                'name': new_name
            }
        },
        upsert=True
    )

def update_player_index(player_id, index):
    player_collection.update_one(
        {
            '_id': player_id
        },
        {
            '$set': {
                'index': index
            }
        },
        upsert=True
    )

def add_player(userid, index):
    player_collection.insert_one({
        '_id': userid,
        'index': index
    })

def get_highest_player_index():
    return player_collection.find().sort(
        [
            (
                'index', -1
            )
        ]
    ).limit(1)[0]['index']
