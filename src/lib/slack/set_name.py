#!/usr/bin/python3.6
import re
from lib.data import characters as character_data
from lib.data import players as player_data


def handle(userid, command_text):
    player = player_data.get_player(userid)
    if player is None:
        return webutil.respond_success('You do not have a player record.')

    command_text_components = re.split(r'[\"\"]', command_text)
    new_name = command_text_components[1]
    player_data.update_player_name(userid, new_name)

    return webutil.respond_success('Alright, <@' + userid + '>, your name is ' + new_name + '!')
