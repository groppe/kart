import logging
from mongodb import player_collection
from mongodb import game_collection

def ranking():
	for player in player_collection.find():
		
		# create the aggregate game query pipeline using the player's id
		game_aggregation_pipeline = [
			{ 
				"$match": { 
					"scores": { 
						"$elemMatch": { 
							"player_id": player['_id']
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
				"$limit": 25 
			},
			{ 
				"$project": {
					"games": 1,
					"scores": { 
						"$filter": {
							"input": '$scores',
							"as": 'score',
							"cond": { '$eq': [ '$$score.player_id', player['_id'] ] }
						}
					}
				}
			}
		]

		result = game_collection.aggregate(game_aggregation_pipeline)
		print(list(result))