#!/usr/bin/python2.7
import json


def lambda_response_success(message):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }


def lambda_response_success_json(body):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(body)
    }


def lambda_response_server_error(message):
    return {
        'statusCode': 500,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }


def lambda_response_unauthorized(message):
    return {
        'statusCode': 404,
        'headers': {
            'Content-Type': 'text/plain',
        },
        'body': message
    }