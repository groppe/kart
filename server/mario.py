#!/usr/bin/python3.6
import dataservice

def bigboard():

	# instantiate the ranking board
	board = []

	# for each player
	for player_cursor in dataservice.all_players():

		# add up the player's game data
		games_played = 0
		total_score = 0.0

		# get their last 25 games
		for game_cursor in dataservice.games_for_player(player_cursor['_id'], 25):

			# get their score from the game
			score = game_cursor['scores'][0]

			# add it to their total
			games_played += int(game_cursor.get('games', 0))
			total_score += float(score.get('score', 0.0))

		# calculate the player's average
		if games_played != 0:
			average = total_score / games_played
		else:
			average = 0.0

		# create the player's board entry
		player = {
			'name': player_cursor['name'],
			'character': player_cursor['character'],
			'average': round(average, 2)
		}

		# add them to the board
		board.append(player)

	# sort by average
	board = sorted(board, key=lambda player: player['average'], reverse=True)

	return board


