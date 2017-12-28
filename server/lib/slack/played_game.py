#!/usr/bin/python2.7
import re
import time
import lib.slack.util as slackutil
from lib import webutil
from lib.data import games as game_data


def handle(command_text):
    command_text = trim_extra_whitespace(command_text)

    result_components = parse_results(command_text)
    race_count = parse_race_count(result_components[0])

    scores = []

    for i in range(1, len(result_components)):
        player_score = {
            'player_id': re.sub('[<@]', '', result_components[1].split(' ')[1].split('|')[0]),
            'score': int(result_components[i].split(' ')[2]),
            'average': round(float(result_components[i].split(' ')[2]) / race_count, 2)
        }

        scores.append(player_score)

    game = {
        'games': race_count,
        'datetime': int(time.time()),
        'scores': scores
    }

    game_data.add_game(game)

    slack_response = slackutil.in_channel_response('*Result*\n')
    return webutil.respond_success(slack_response)


def trim_extra_whitespace(text):
    return ' '.join(text.split())


def parse_results(text):
    return text.split(',')


def parse_race_count(text):
    return int(text.split(' ')[1], 0)
    


