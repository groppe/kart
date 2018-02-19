#!/usr/bin/python3.6
import re
import lib.webutil as webutil
from lib.data import characters as character_data
from lib.data import players as player_data


def handle(userid, command_text):
    player = player_data.get_player(userid)
    if player is None:
        return webutil.respond_success('You do not have a player record.')

    command_text_components = re.split(r'[\"\"]', command_text)
    character_name = command_text_components[1]
    if character_exists(character_name):
        return webutil.respond_success('A character with that name does not exist.')

    player_data.update_player_character(userid, character_name)
    return webutil.respond_success('Alright, <@' + userid + '>, your character is ' + character_name + '!')

def character_exists(character_name):
    character = character_data.get_character_by_name(character_name)
    if character is None:
        return False
    else:
        return True