#!/usr/bin/python3.6
import json
import lib.common.web as webutil
import logging
from lib import rank


@webutil.log_event
def average(event, context):
    ranking_average = {
        'rankings': rank.average_individual()
    }
    return webutil.respond_success_json(json.dumps(ranking_average))
