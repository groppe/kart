#!/usr/bin/python2.7
import json
import unittest

from lib import webutil as webutil


class RankTests(unittest.TestCase):

    def testRespondSuccess(self):

        # Arrange
        message = 'message'
        expected_result = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain',
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
            },
            'body': json.dumps(body)
        }

        # Act
        result = webutil.respond_success_json(body)

        # Assert
        self.assertDictEqual(expected_result, result)

    def testRespondServerError(self):

        # Arrange
        message = 'message'
        expected_result = {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'text/plain',
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
            },
            'body': message
        }

        # Act
        result = webutil.respond_unauthorized(message)

        # Assert
        self.assertDictEqual(expected_result, result)
