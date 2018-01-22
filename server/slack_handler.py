#!/usr/bin/python2.7
import re
import json
import lib.slack.add_character as add_character
import lib.slack.characters as characters
import lib.slack.help as help
import lib.slack.played_game as played_game
import lib.slack.rankings as rankings
import lib.slack.set_character as set_character
import lib.slack.set_name as set_name
import lib.slack.util as slackutil
import lib.webutil as webutil
import logging

# compile regular expressions for slash command parameter strings
pattern_help = re.compile('^help$')
pattern_ranking = re.compile('^rankings$')
pattern_played = re.compile('^(played\s+\d+\s+games)((,\s+(<@\w+\|\w+>)\s+([0-9]+))+)$')
pattern_characters = re.compile('^characters$')
pattern_add_character = re.compile('^(add character\\s)(\".*\"\\s)([^\\s]+)$')
pattern_set_name = re.compile('^my name is \".*\"$')
pattern_set_character = re.compile('^my character is \".*\"$')


def handle(event, context):
    input_data = slackutil.parse_input(event['body'])

    logging.info(json.dumps(input_data))

    if slackutil.validate_slack_token(input_data) is False:
        return webutil.respond_unauthorized("Invalid Slack token")

    command_text = input_data.get('text', '')

    if pattern_ranking.match(command_text):
        return rankings.handle()
    elif pattern_played.match(command_text):
        return played_game.handle(command_text)
    elif pattern_characters.match(command_text):
        return characters.handle()
    elif pattern_add_character.match(command_text):
        return add_character.handle(command_text)
    elif pattern_set_name.match(command_text):
        return set_name.handle(command_text)
    elif pattern_set_character.match(command_text):
        return set_character.handle(command_text)
    else:
        return help.handle()
