#!/usr/bin/python3.6
import json
import logging
from lib import webutil as webutil
from lib.data import games as game_data

def create(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def all(event, context):
    queryStringParameters = event.get('queryStringParameters') or {}
    size = queryStringParameters.get('size', 25)
    page = queryStringParameters.get('page', 0)
    player_id = queryStringParameters.get('player_id')

    query_criteria = {}
    if player_id is not None:
        query_criteria['player_id'] = player_id

    games = game_data.games_in_range(query_criteria, size, page)

    response = {
        'games': list(games),
        'player_id': player_id,
        'size': size,
        'page': page
    }
    return webutil.respond_success_json(json.dumps(response))

def get(event, context):
    game_id = event['pathParameters']['id']
    game = game_data.game_by_id(game_id)
    if game is None:
        return webutil.respond_not_found('a game with that id does not exist')
    
    return webutil.respond_success_json(game)

def update(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def delete(event, context):
    game_id = event['pathParameters']['id']
    if not game_data.game_by_id(game_id):
        return webutil.respond_not_found('a game with that id does not exist')

    game_data.delete_game(game_id)

    return webutil.respond_success(game_id)