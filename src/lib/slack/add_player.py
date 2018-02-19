#!/usr/bin/python3.6
import re
import lib.webutil as webutil
import lib.slack.util as slackutil
from lib.data import players as player_data

def handle(command_text):
    command_string_components = split_add_player_string(command_text)
    new_player_id = extract_slack_user_id(command_string_components)

    if player_exists(new_player_id):
        return webutil.respond_success('A player record for <@' + new_player_id + '> already exists.')

    index_of_new_player = determine_players_index()
    player_data.add_player_with_id(new_player_id, index_of_new_player)
    return webutil.respond_success_json(slackutil.in_channel_response('Alright, <@' + new_player_id + '> is ready to play!'))


def split_add_player_string(command_string_components):
    return command_string_components.split(' ')


def extract_slack_user_id(command_string_components):
    return re.sub('[<@]', '', command_string_components[2].split('|')[0])


def player_exists(player_id):
    player = player_data.get_player(player_id)
    if player is None:
        return False
    else:
        return True


def determine_players_index():
    highest_current_index = player_data.get_highest_player_index()
    return highest_current_index + 1
