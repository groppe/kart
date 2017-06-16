#!/usr/bin/python3.6
import logging
from .mongodb import player_collection
from .mongodb import game_collection

def all_players():
	return player_collection.find()