#!/usr/bin/python2.7
from mongodb import player_collection

def all_players():
	return player_collection.find()