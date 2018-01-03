#!/usr/bin/python2.7
import logging
import os
import sys
import urlparse

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

if SLACK_TOKEN is None:  # pragma: no cover
    logging.critical("SLACK_TOKEN environment variable must be set")
    sys.exit(1)


def parse_input(data):
    parsed = urlparse.parse_qsl(data, keep_blank_values=True)
    result = {}
    for item in parsed:
        result[item[0]] = item[1]
    return result


def validate_slack_token(request_data):
    if request_data.get('token', '') == SLACK_TOKEN:
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