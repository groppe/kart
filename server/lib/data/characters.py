#!/usr/bin/python2.7
from lib.data.mongodb import character_collection


def all_characters():
    return character_collection.find()


def add_character(character):
    return character_collection.insert_one(character)
