#!/usr/bin/python3.6
import json
import logging
import lib.common.web as webutil
from bson.json_util import dumps
from lib.data import characters as character_data


@webutil.log_event
def create(event, context):
    return webutil.respond_not_implemented()


@webutil.log_event
def all(event, context):
    all_characters = character_data.all_characters()
    response = {
        'characters': all_characters
    }
    return webutil.respond_success_json(dumps(response))


@webutil.log_event
def get(event, context):
    return webutil.respond_not_implemented()


@webutil.log_event
def update(event, context):
    return webutil.respond_not_implemented()


@webutil.log_event
def delete(event, context):
    return webutil.respond_not_implemented()