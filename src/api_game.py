#!/usr/bin/python2.7
import re
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
    games = game_data.games_in_range(size, page)
    response = {
        'games': list(games),
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