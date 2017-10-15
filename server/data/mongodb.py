#!/usr/bin/python2.7
import sys
import os
import logging
from pymongo import MongoClient

MONGO_URI = os.environ.get('MARIO_MONGO_URI')
MONGO_DB = os.environ.get('MARIO_MONGO_DB')

MONGO_COLLECTION_GAME = 'GAME'
MONGO_COLLECTION_PLAYER = 'PLAYER'
MONGO_COLLECTION_CHARACTER = 'CHARACTER'

# verify database connection environment variables
if MONGO_URI is None:
	logging.critical("MARIO_MONGO_URI environment variable must be set")
	sys.exit(1)

if MONGO_DB is None:
	logging.critical("MARIO_MONGO_URI environment variable must be set")
	sys.exit(1)

# connect to the database
client = MongoClient(MONGO_URI)
database = client[MONGO_DB]

# set references to the collections
player_collection = database[MONGO_COLLECTION_PLAYER]
game_collection = database[MONGO_COLLECTION_GAME]
character_collection = database[MONGO_COLLECTION_CHARACTER]