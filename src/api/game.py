#!/usr/bin/python3.6
import json
import logging
import re
from lib import webutil as webutil
from lib.data import games as game_data
from bson.json_util import dumps

def create(event, context):
    logging.critical(event)

    request_body = webutil.parse_event_for_request_body(event)
    if not request_body:
        return webutil.respond_bad_request('to add a game, include the number of games and at least two players')

    request_data = json.loads(request_body)
    slack_id = request_data.get('slack_id', None)
    if not slack_id:
        return webutil.respond_bad_request('to create a player, include at least their Slack id')

def all(event, context):
    queryStringParameters = event.get('queryStringParameters') or {}
    size = int(queryStringParameters.get('size') or 25)
    page = int(queryStringParameters.get('page') or 0)
    player_id = queryStringParameters.get('player_id')

    if not player_id:
        any_player = '.*'
        games = game_data.games_for_player(any_player, size, page)
    else:
        games = game_data.games_for_player(player_id, size, page)

    response = {
        'games': list(games),
        'player_id': player_id,
        'size': size,
        'page': page
    }
    return webutil.respond_success_json(dumps(response))

def get(event, context):
    game_id = event['pathParameters']['id']
    game = game_data.game_by_id(game_id)
    if game is None:
        return webutil.respond_not_found('a game with that id does not exist')
    
    return webutil.respond_success_json(dumps(game))

def update(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def delete(event, context):
    game_id = event['pathParameters']['id']
    if not game_data.game_by_id(game_id):
        return webutil.respond_not_found('a game with that id does not exist')

    game_data.delete_game(game_id)

    return webutil.respond_success(game_id)