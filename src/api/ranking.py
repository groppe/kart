#!/usr/bin/python3.6
import json
import logging
from lib import rank
from lib import webutil

def average(event, context):
    ranking_average = {
        'rankings': rank.average_individual()
    }
    return webutil.respond_success_json(ranking_average)
