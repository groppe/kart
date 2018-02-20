#!/usr/bin/python3.6
import json
import logging
from bson.json_util import dumps
from lib import webutil as webutil
from lib.data import characters as character_data

def create(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def all(event, context):
    logging.critical(event)
    all_characters = character_data.all_characters()
    response = {
        'characters': all_characters
    }
    return webutil.respond_success_json(dumps(response))

def get(event, context):
    logging.critical(event)
    id = event['pathParameters']['id']

def update(event, context):
    logging.critical(event)
    data = json.loads(event['body'])

def delete(event, context):
    logging.critical(event)
    id = event['pathParameters']['id']