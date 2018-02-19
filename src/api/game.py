#!/usr/bin/python3.6
import json
import logging
from lib import webutil as webutil
from lib.data import games as game_data

def create(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def all(event, context):
    logging.critical(event)

    size = event['queryStringParameters'].get('size', 25)
    page = event['queryStringParameters'].get('page', 0)
    player_id = event['queryStringParameters'].get('player_id', None)

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
    logging.critical(event)
    id = event['pathParameters']['id']

def update(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def delete(event, context):
    logging.critical(event)
    id = event['pathParameters']['id']