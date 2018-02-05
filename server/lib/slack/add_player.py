#!/usr/bin/python2.7
import re
import lib.webutil as webutil
import slack.util as slackutil
from lib.data import players as player_data

def handle(command_text):
    player_components = command_text.split(' ')
    new_player_id = re.sub('[<@]', '', player_components[2].split('|')[0])

    player = player_data.get_player(new_player_id)
    if player is not None:
        return webutil.respond_success('A player record for <@' + new_player_id + '> already exists.')

    player_data.add_player(new_player_id)
    return webutil.respond_success(slackutil.in_channel_response('Alright, <@' + new_player_id + '> is ready to play!'))
