#!/usr/bin/python3.6
import json
import logging
import os
import sys
from functools import wraps
from urllib import parse as urlparse

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

if SLACK_TOKEN is None:  # pragma: no cover
    logging.critical("SLACK_TOKEN environment variable must be set")
    sys.exit(1)


def parse_and_log_slack_body(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        event = args[0]
        slack_request = parse_input(event['body'])
        logging.critical(json.dumps(slack_request))
        return func(*args, **kwargs)
    return wrapper


def parse_input(data):
    parsed = urlparse.parse_qsl(data, keep_blank_values=True)
    result = {}
    for item in parsed:
        result[item[0]] = item[1]
    return result


def validate_slack_token(slack_request):
    if slack_request.get('token', '') == SLACK_TOKEN:
        return True
    else:
        return False


def in_channel_response(text):
    return {
        'response_type': 'in_channel',
        'text': text
    }


def ephemeral_response(text):
    return {
        'response_type': 'ephemeral',
        'text': text
    }