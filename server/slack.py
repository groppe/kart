#!/usr/bin/python2.7
import datetime
import json
import kartlogic.rank
import logging
import re
import prettytable
import util.web as webutil
import util.slack as slackutil

# compile regular expressions for slash command parameter strings
pattern_help = re.compile('^help$')
pattern_ranking = re.compile('^rankings$')
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
        return handle_played(command_text)
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
    help_text = '*Usage:* /mario <command>\n*Commands:*\n```'
    help_text += '\n1. rankings'
    help_text += '\n2. played <#> games, <user1> <score1>, <user2> <score2>[, <user3> <score3>]'
    help_text += '\n3. characters'
    help_text += '\n4. add character "<character name>" <character image url>'
    help_text += '\n5. my character is "<valid character name>"'
    help_text += '\n6. my name is "<name you want to be called>"'
    help_text += '```'
    return webutil.respond_success(help_text)


def handle_rankings():
    # retrieve the rankings
    rankings = kartlogic.rank.average_individual()

    # initialize the text table
    table = prettytable.PrettyTable(['Rank', 'Player', 'Character', 'Average'])

    # add each ranking entry to the table
    for index, player in enumerate(rankings):
        table.add_row([(index + 1), player['name'], player['character'], player['average']])

    # covert the table to format that Slack will understand
    table_string = '```' + table.get_string(border=True) + '```'
    slack_response = slackutil.in_channel_response(table_string)

    return webutil.respond_success_json(slack_response)


def handle_played(command_text):
    # condense whitespace
    command_text = ' '.join(command_text.split())

    components = command_text.split(',')
    race_count = int(components[0].split(" ")[1], 0)

    scores = []

    for i in range(1, len(components)):
        player_score = {
            'player_id': re.sub('[<@]', '', components[1].split(' ')[1].split('|')[0]),
            'score': components[i].split(' ')[2],
            'average': round(float(components[i].split(' ')[2]) / race_count, 2)
        }

        scores.append(player_score)

    game = {
        'games': race_count,
        'datetime': datetime.datetime.now(),
        'scores': scores
    }

    logging.critical(json.dumps(game))


def handle_characters():
    return webutil.respond_success('Characters')


def handle_add_character():
    return webutil.respond_success('Add Character')


def handle_my_name():
    return webutil.respond_success('My Name')


def handle_my_character():
    return webutil.respond_success('My Character')
