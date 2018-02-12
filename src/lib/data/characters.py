#!/usr/bin/python2.7
from lib.data.mongodb import character_collection


def all_characters():
    return character_collection.find()


def add_character(character):
    return character_collection.insert_one(character)


def get_character(character_id):
    return character_collection.find_one({
        '_id': character_id
    })


def get_character_by_name(name):
    return character_collection.find_one({
        'name': name
    })

