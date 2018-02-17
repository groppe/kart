#!/usr/bin/python3.6
import re
import json
import logging
import lib.slack.add_player as player_service
import lib.slack.set_character as character_service
from lib import webutil as webutil
from lib.data import players as player_data

def create(event, context):
    logging.critical(event)
    
    request_body = webutil.parse_event_for_request_body(event)
    if not request_body:
        return webutil.respond_bad_request('to create a player, include at least their Slack id')

    request_data = json.loads(request_body)
    slack_id = request_data.get('slack_id', None)
    if not slack_id:
        return webutil.respond_bad_request('to create a player, include at least their Slack id')

    if player_service.player_exists(slack_id):
        return webutil.respond_conflict('a player with this Slack id already exists')

    character_name = request_data.get('character')
    if not character_service.character_exists(character_name):
        return webutil.respond_not_found('a character with the name you specified for this player does not exist')

    new_player = {
        '_id': slack_id,
        'name': request_data.get('name'),
        'character': character_name,
        'active': True,
        'index': player_service.determine_players_index()
    }

    player_data.add_player(new_player)

    return webutil.respond_success(slack_id)

def all(event, context):
    logging.critical(event)
    all_players = player_data.all_players()
    response = {
        'players': list(all_players)
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
