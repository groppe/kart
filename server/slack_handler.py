#!/usr/bin/python2.7
import re
import json
import logging
import lib.slack.add_character as add_character
import lib.slack.characters as characters
import lib.slack.help as helper
import lib.slack.played_game as played_game
import lib.slack.rankings as rankings
import lib.slack.set_character as set_character
import lib.slack.set_name as set_name
import lib.slack.util as slackutil
import lib.webutil as webutil

# compile regular expressions for slash command parameter strings
PATTERN_HELP = re.compile('^help$')
PATTERN_RANKING = re.compile('^rankings$')
PATTERN_PLAYED = re.compile('^(played\s+\d+\s+games)((,\s+(<@\w+\|\w+>)\s+([0-9]+))+)$')
PATTERN_CHARACTERS = re.compile('^characters$')
PATTERN_ADD_CHARACTER = re.compile('^(add character\\s)(\".*\"\\s)([^\\s]+)$')
PATTERN_SET_NAME = re.compile('^my name is \".*\"$')
PATTERN_SET_CHARACTER = re.compile('^my character is \".*\"$')


def handle(event, context):
    input_data = slackutil.parse_input(event['body'])

    logging.info(json.dumps(input_data))

    if slackutil.validate_slack_token(input_data) is False:
        return webutil.respond_unauthorized("Invalid Slack token")

    command_text = input_data.get('text', '')

    if PATTERN_RANKING.match(command_text):
        return rankings.handle()
    elif PATTERN_PLAYED.match(command_text):
        return played_game.handle(command_text)
    elif PATTERN_CHARACTERS.match(command_text):
        return characters.handle()
    elif PATTERN_ADD_CHARACTER.match(command_text):
        return add_character.handle(command_text)
    elif PATTERN_SET_NAME.match(command_text):
        return set_name.handle(command_text)
    elif PATTERN_SET_CHARACTER.match(command_text):
        return set_character.handle(command_text)
    else:
        return helper.handle()
