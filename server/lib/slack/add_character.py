#!/usr/bin/python2.7
import re
import lib.webutil as webutil
import lib.slack.util as slackutil
from lib.data import characters as character_data


def handle(command_text):
    character_components = re.split(r'[\"\"]', command_text)
    character = {
        'name': character_components[1],
        'image': character_components[2].lstrip()
    }
    character_data.add_character(character)
    slack_body = slackutil.in_channel_response_as_user(
        'I\'m alive!',
        character_components[1],
        character_components[2].lstrip()
    )
    return webutil.respond_success_json(slack_body)
