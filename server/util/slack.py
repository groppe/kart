#!/usr/bin/python2.7


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