#!/usr/bin/python2.7
from lib.data import characters as character_data
import lib.webutil as webutil
import lib.slack.util as slackutil


def handle():
    characters = ''
    for character in character_data.all_characters():
        character_string = '-' + character['name'] + '\n'
        characters += character_string
    slack_body = slackutil.ephemeral_response(characters)
    return webutil.respond_success(slack_body)
