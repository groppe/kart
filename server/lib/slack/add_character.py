#!/usr/bin/python2.7
import re
import lib.webutil as webutil
import lib.slack.util as slackutil
from lib.data import characters as character_data


def handle(command_text):
    command_text_components = re.split(r'[\"\"]', command_text)
    character_name = command_text_components[1]
    character_icon = re.sub(r'[<>\s]', '', command_text_components[2])
    character = {
        'name': character_name,
        'image': character_icon
    }
    character_data.add_character(character)
    slack_body = slackutil.in_channel_response_as_user(
        'I\'m alive!',
        character_name,
        character_icon
    )
    return webutil.respond_success_json(slack_body)
