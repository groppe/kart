#!/usr/bin/python2.7
import mongodb

# drop existing dev databases
mongodb.player_collection_dev.remove()
mongodb.game_collection_dev.remove()
mongodb.character_collection_dev.remove()

all_players = mongodb.player_collection.find()
for player in all_players:
	mongodb.player_collection_dev.insert(player)

all_games = mongodb.game_collection.find()
for game in all_games:
	mongodb.game_collection_dev.insert(game)

all_characters = mongodb.character_collection.find()
for character in all_characters:
	mongodb.character_collection_dev.insert(character)