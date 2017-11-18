#!/usr/bin/python2.7
import json
import kartlogic.rank
import logging
import re
import prettytable
import util.web as webutil
import util.slack as slackutil

# compile regular expressions for slash command parameter strings
pattern_help = re.compile('^help$')
pattern_ranking = re.compile('^ranking$')
pattern_played = re.compile('^(played\s+\d+\s+games)((,\s+(<@\w+\|\w+>)\s+([0-9]+))+)$')
pattern_characters = re.compile('^characters$')
pattern_add_character = re.compile('^(add character\\s)(\".*\"\\s)([^\\s]+)$')
pattern_my_name = re.compile('^my name is \".*\"$')
pattern_my_character = re.compile('^my character is \".*\"$')


def handler(event, context):
    input_data = slackutil.parse_input(event['body'])

    if slackutil.validate_slack_token(input_data) is False:
        return webutil.respond_unauthorized("Invalid Slack token")

    command_text = input_data.get('text', 'help')
    if pattern_ranking.match(command_text):
        return handle_rankings()
    elif pattern_played.match(command_text):
        return handle_played()
    elif pattern_characters.match(command_text):
        return handle_characters()
    elif pattern_add_character.match(command_text):
        return handle_add_character()
    elif pattern_my_name.match(command_text):
        return handle_my_name()
    elif pattern_my_character.match(command_text):
        return handle_my_character()
    else:
        return handle_help()


def handle_help():
    return webutil.respond_success('Help')


def handle_rankings():
    rankings = kartlogic.rank.average_individual()
    table = prettytable.PrettyTable(['Rank', 'Player', 'Character', 'Average'])
    for index, player in enumerate(rankings):
        table.add_row([(index + 1), player['name'], player['character'], player['average']])
    table_string = '```' + table.get_string(border=True) + '```'
    slack_response = slackutil.in_channel_response(table_string)
    return webutil.respond_success_json(slack_response)


def handle_played():
    return webutil.respond_success('Played')


def handle_characters():
    return webutil.respond_success('Characters')


def handle_add_character():
    return webutil.respond_success('Add Character')


def handle_my_name():
    return webutil.respond_success('My Name')


def handle_my_character():
    return webutil.respond_success('My Character')
