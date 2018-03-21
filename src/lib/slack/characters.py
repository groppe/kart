#!/usr/bin/python3.6
import json
from lib.data import characters as character_data
import lib.common.web as webutil
import lib.common.slack as slackutil


def handle():
    characters = ''
    for character in character_data.all_characters():
        character_string = '-' + character['name'] + '\n'
        characters += character_string
    slack_body = slackutil.ephemeral_response(characters)
    return webutil.respond_success_json(json.dumps(slack_body))
