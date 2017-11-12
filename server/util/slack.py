#!/usr/bin/python2.7
import os
import urllib.parse

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')


def parse_input(data):
    parsed = urllib.parse.parse_qsl(data, keep_blank_values=True)
    result = {}
    for item in parsed:
        result[item[0]] = item[1]
    return result


def validate_token(body):
    return True


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