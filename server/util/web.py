#!/usr/bin/python2.7
import json


def respond_success(message):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }


def respond_success_json(body):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(body)
    }


def respond_server_error(message):
    return {
        'statusCode': 500,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }


def respond_unauthorized(message):
    return {
        'statusCode': 401,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }