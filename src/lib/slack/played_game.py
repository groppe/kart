#!/usr/bin/python3.6
import json
import re
import time
import lib.slack.util as slackutil
from lib import webutil
from lib.data import games as game_data
from lib.data import players as player_data


def handle(command_text):
    command_text = trim_extra_whitespace(command_text)

    result_components = parse_results(command_text)
    race_count = parse_race_count(result_components[0])

    scores = []

    for i in range(1, len(result_components)):
        player_score = {
            'player_id': re.sub('[<@]', '', result_components[i].split(' ')[1].split('|')[0]),
            'score': int(result_components[i].split(' ')[2]),
            'average': round(float(result_components[i].split(' ')[2]) / race_count, 2)
        }

        scores.append(player_score)

    game = {
        'games': race_count,
        'datetime': int(time.time()) * 1000,
        'scores': scores
    }

    game_data.add_game(game)

    scores = sorted(scores, key=lambda k: k['average'], reverse=True)

    response_text = 'A game of *' + str(game.get('games')) + '* races was played! Average scores:'
    for score in scores:
        player_cursor = player_data.get_player(score['player_id']) or {}
        response_text += '\n' + player_cursor.get('name', '<Unknown>')
        response_text += ': ' + str(score['average'])

    slack_body = slackutil.in_channel_response(response_text)
    return webutil.respond_success_json(json.dumps(slack_body))


def trim_extra_whitespace(text):
    return ' '.join(text.split())


def parse_results(text):
    return text.split(',')


def parse_race_count(text):
    return int(text.split(' ')[1])
    


