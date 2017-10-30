#!/usr/bin/python2.7
import unittest
import kartlogic.rank as rank


class RankTests(unittest.TestCase):

    def testInstantiateEmptyArray(self):

        # Arrange
        empty_array = []

        # Act
        result = rank.instantiate_empty_array()

        # Assert
        self.assertEqual(result, empty_array)

    def testGetPlayerScoreEntry(self):

        # Arrange
        game = {
            'scores': [4]
        }

        # Act
        result = rank.get_player_score_entry(game)

        # Assert
        self.assertEqual(result, 4)

    def testGetNumberOfGamesPlayed(self):

        # Arrange
        count = 5
        cursor = {
            'games': count
        }

        # Act
        result = rank.get_number_of_games_played(cursor)

        # Assert
        self.assertEqual(result, count)

    def testGetPlayerScore(self):

        # Arrange
        score = 25
        score_entry = {
            'score': score
        }

        # Act
        result = rank.get_player_score(score_entry)

        # Assert
        self.assertEquals(result, score)

    def testCalculateAverage_WhenGamesPlayed_ReturnsAverage(self):

        # Arrange
        games_played = 5
        score = 75

        # Act
        result = rank.calculate_average(games_played, score)

        # Assert
        self.assertEqual(result, 14.00)

    def testCalculateAverage_WhenNoGamesPlayed_ReturnsZero(self):

        # Arrange
        games_played = 0
        score = 0

        # Act
        result = rank.calculate_average(games_played, score)

        # Assert
        self.assertEqual(result, 0.00)

    def testGetPlayerId(self):

        # Arrange
        id = 'U33213'
        cursor = {
            '_id': id
        }

        # Act
        result = rank.get_player_id(cursor)

        # Assert
        self.assertEqual(result, id)

    def testGetPlayerName_WhenCursorContainsName_ReturnsName(self):

        # Arrange
        name = 'groppe'
        cursor = {
            'name': name
        }

        # Act
        result = rank.get_player_name(cursor)

        # Assert
        self.assertEqual(result, name)

    def testGetPlayerName_WhenCursorDoesNotContainName_ReturnsUnknown(self):

        # Arrange
        cursor = {}

        # Act
        result = rank.get_player_name(cursor)

        # Assert
        self.assertEqual(result, '<Unknown>')

    def testGetPlayerCharacter_WhenCursorContainsCharacter_ReturnsCharacter(self):

        # Arrange
        character = 'link'
        cursor = {
            'character': character
        }

        # Act
        result = rank.get_player_character(cursor)

        # Assert
        self.assertEqual(result, character)

    def testGetPlayerCharacter_WhenCursorDoesNotContainCharacter_ReturnsUnknown(self):

        # Arrange
        cursor = {}

        # Act
        result = rank.get_player_character(cursor)

        # Assert
        self.assertEqual(result, '<Unknown>')

    def testCreatePlayerEntry(self):

        # Arrange
        id = 'U39293'
        character = 'link'
        name = 'groppe'
        cursor = {
            '_id': id,
            'name': name,
            'character': character
        }
        average = 1.23

        # Act
        result = rank.create_player_entry(cursor, average)

        # Assert
        player = {
            'id': id,
            'name': name,
            'character': character,
            'average': average
        }
        self.assertDictEqual(result, player)


def main():
    unittest.main()


if __name__ == '__main__':
    main()