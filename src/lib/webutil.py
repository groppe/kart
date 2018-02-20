#!/usr/bin/python3.6
import json


def parse_event_for_request_body(event):
    return event.get('body', None)


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
        'body': body
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


def respond_bad_request(message):
    return {
        'statusCode': 400,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }


def respond_conflict(message):
    return {
        'statusCode': 409,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }


def respond_not_found(message):
    return {
        'statusCode': 404,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }
