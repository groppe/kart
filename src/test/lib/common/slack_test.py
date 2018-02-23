#!/usr/bin/python3.6
import os
import unittest
from lib.slack import util as slackutil

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')


class RankTests(unittest.TestCase):

    def testParseInput_WhenDataEmpty_ReturnsEmptyDictionary(self):

        # Arrange
        data = ''

        # Act
        result = slackutil.parse_input(data)

        # Assert
        self.assertDictEqual(result, {})

    def testParseInput_WhenDataHasOneItem_ReturnsDictionaryWithItem(self):

        # Arrange
        data = 'team_id=T036F5PR0'
        expected_result = {
            'team_id': 'T036F5PR0'
        }

        # Act
        result = slackutil.parse_input(data)

        # Assert
        self.assertDictEqual(result, expected_result)

    def testParseInput_WhenDataHasTwoItems_ReturnsDictionaryOfItems(self):

        # Arrange
        data = 'team_id=T036F5PR0&token=583jd93hro2fm3'
        expected_result = {
            'team_id': 'T036F5PR0',
            'token': '583jd93hro2fm3'
        }

        # Act
        result = slackutil.parse_input(data)

        # Assert
        self.assertDictEqual(result, expected_result)

    def testValidateSlackToken_WhenTokenValid_ReturnsTrue(self):

        # Arrange
        request_data = {
            'token': SLACK_TOKEN
        }

        # Act
        result = slackutil.validate_slack_token(request_data)

        # Assert
        self.assertTrue(result)

    def testValidateSlackToken_WhenTokenInvalid_ReturnsFalse(self):

        # Arrange
        test_token = 'invalid'
        request_data = {
            'token': test_token
        }

        # Act
        result = slackutil.validate_slack_token(request_data)

        # Assert
        self.assertFalse(result)

    def testValidateSlackToken_WhenTokenNotPresent_ReturnsFalse(self):

        # Arrange
        request_data = {}

        # Act
        result = slackutil.validate_slack_token(request_data)

        # Assert
        self.assertFalse(result)

    def testInChannelResponse(self):

        # Arrange
        text = 'test text'
        in_channel_response = {
            'response_type': 'in_channel',
            'text': text
        }

        # Act
        result = slackutil.in_channel_response(text)

        # Assert
        self.assertDictEqual(result, in_channel_response)

    def testEphemeralResponse(self):

        # Arrange
        text = 'test text'
        ephemeral_response = {
            'response_type': 'ephemeral',
            'text': text
        }

        # Act
        result = slackutil.ephemeral_response(text)

        # Assert
        self.assertDictEqual(result, ephemeral_response)