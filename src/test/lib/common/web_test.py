#!/usr/bin/python3.6
import json
import unittest
from lib.common import web as webutil


class RankTests(unittest.TestCase):

    def testRespondSuccess(self):

        # Arrange
        message = 'message'
        expected_result = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain',
                'Access-Control-Allow-Origin': '*'
            },
            'body': message
        }

        # Act
        result = webutil.respond_success(message)

        # Assert
        self.assertDictEqual(expected_result, result)

    def testRespondSuccessJson(self):

        # Arrange
        body = {
            'array': [0, 1, 2],
            'string': 'something'
        }
        expected_result = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(body)
        }

        # Act
        result = webutil.respond_success_json(json.dumps(body))

        # Assert
        self.assertDictEqual(expected_result, result)

    def testRespondServerError(self):

        # Arrange
        message = 'message'
        expected_result = {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'text/plain',
                'Access-Control-Allow-Origin': '*'
            },
            'body': message
        }

        # Act
        result = webutil.respond_server_error(message)

        # Assert
        self.assertDictEqual(expected_result, result)

    def testRespondUnauthorized(self):

        # Arrange
        message = 'message'
        expected_result = {
            'statusCode': 401,
            'headers': {
                'Content-Type': 'text/plain',
                'Access-Control-Allow-Origin': '*'
            },
            'body': message
        }

        # Act
        result = webutil.respond_unauthorized(message)

        # Assert
        self.assertDictEqual(expected_result, result)
