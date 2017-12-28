#!/usr/bin/python2.7
import unittest
import lib.slack.played_game as played_game


class PlayedGameTest(unittest.TestCase):

    def test_TrimExtraWhitespace(self):
        
        # Arrange
        text = ' played  5  games,  <@U7I9H|Groppe>  75,  <@U7I9H|Boone>  65,  <@U7I9H|Mario> 55 '
        expected_text = 'played 5 games, <@U7I9H|Groppe> 75, <@U7I9H|Boone> 65, <@U7I9H|Mario> 55'

        # Act
        trimmed_text = played_game.trim_extra_whitespace(text)

        # Assert
        self.assertEqual(trimmed_text, expected_text)


    def test_ParseResults(self):

        # Arrange
        text = 'played 5 games, <@U7I9H|Groppe> 75, <@U7I9H|Boone> 65, <@U7I9H|Mario> 55'
        expected_result_components = ['played 5 games', ' <@U7I9H|Groppe> 75', ' <@U7I9H|Boone> 65', ' <@U7I9H|Mario> 55']
        # Act
        result_components = played_game.parse_results(text)

        # Assert
        self.assertItemsEqual(result_components,expected_result_components)
