#!/usr/bin/python2.7
import re
import json
import logging
from lib import webutil as webutil
from lib.data import players as player_data

def create(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def all(event, context):
    logging.critical(event)
    all_players = player_data.all_players()
    return webutil.respond_success_json(json.dumps(list(all_players)))

def get(event, context):
    logging.critical(event)
    id = event['pathParameters']['id']

def update(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def delete(event, context):
    logging.critical(event)
    id = event['pathParameters']['id']