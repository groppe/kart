#!/usr/bin/python3.6
import logging
from mongodb import player_collection
from mongodb import game_collection

def all_players():
	return player_collection.find()

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
						"cond": { '$eq': [ '$$score.player_id', player_id ] }
					}
				}
			}
		}
	])