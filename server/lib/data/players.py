#!/usr/bin/python2.7
from mongodb import player_collection


def all_players():
    return player_collection.find()


def get_player(player_id):
    return player_collection.find({
        '_id': player_id
    })


def upsert_player_name(player_id, name):
	return player_collection.update()


def upsert_player_character(player_id, character):
	return player_collection.update()
