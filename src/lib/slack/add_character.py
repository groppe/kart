#!/usr/bin/python3.6
import json
import re
import lib.webutil as webutil
import lib.slack.util as slackutil
from lib.data import characters as character_data


def handle(command_text):
    command_text_components = re.split(r'[\"\"]', command_text)
    character_name = command_text_components[1]
    character_icon = re.sub(r'[<>\s]', '', command_text_components[2])
    character = character_data.get_character_by_name(character_name)
    if character.count() > 0:
        return webutil.respond_success("A character with this name already exists")
    new_character = {
        'name': character_name,
        'image': character_icon
    }
    character_data.add_character(new_character)
    slack_body = slackutil.in_channel_response('Successfully added \"' + character_name + '\" as a character.')
    return webutil.respond_success_json(json.dumps(slack_body))
