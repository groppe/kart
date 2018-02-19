#!/usr/bin/python3.6
from lib.data.mongodb import player_collection


def all_players():
    return player_collection.find({ 'active': True })


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

def add_player(new_player):
    player_collection.insert_one(new_player)

def update_player(player_id, updated_player):
    player_collection.update_one(
        {
            '_id': player_id
        },
        {
            '$set': updated_player
        },
        upsert=True
    )

def add_player_with_id(userid, index):
    player_collection.insert_one({
        '_id': userid,
        'active': True,
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

def set_player_active(player_id):
    update_player(player_id, {
                'active': True
    })

def set_player_inactive(player_id):
    update_player(player_id, {
                'active': False
    })
