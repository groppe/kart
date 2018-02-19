#!/usr/bin/python3.6
import unittest
import lib.rank as rank


class RankTests(unittest.TestCase):

    def testInstantiateEmptyArray(self):

        # Arrange
        empty_array = []

        # Act
        result = rank.instantiate_empty_array()

        # Assert
        self.assertEqual(result, empty_array)

    def testCalculateAverageScoreForPlayer_WhenNoGames_AverageZero(self):

        # Arrange
        games = []

        # Act
        result = rank.calculate_average_score_for_player(games)

        # Assert
        self.assertEqual(result, 0)

    def testCalculateAverageScoreForPlayer_WhenOneGame_AverageIsGameScore(self):

        # Arrange
        games = [
            {
                'games': 5,
                'scores': [
                    {
                        'score': "75"
                    }
                ]
            }
        ]

        # Act
        result = rank.calculate_average_score_for_player(games)

        # Assert
        self.assertEqual(result, 15)

    def testCalculateAverageScoreForPlayer_WhenMultipleGames_AverageIsCalculated(self):

        # Arrange
        games = [
            {
                'games': 5,
                'scores': [
                    {
                        'score': "75"
                    }
                ]
            },
            {
                'games': 5,
                'scores': [
                    {
                        'score': "65"
                    }
                ]
            },
            {
                'games': 5,
                'scores': [
                    {
                        'score': "60"
                    }
                ]
            }
        ]

        # Act
        result = rank.calculate_average_score_for_player(games)

        # Assert
        self.assertEqual(result, 13.33)

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
        self.assertEqual(result, score)

    def testCalculateAverage_WhenGamesPlayed_ReturnsAverage(self):

        # Arrange
        games_played = 5
        score = 75

        # Act
        result = rank.calculate_average(games_played, score)

        # Assert
        self.assertEqual(result, 15.00)

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

    def testAverageIndividual_ReturnsArray(self):

        # Act
        result = rank.average_individual()

        # Assert
        self.assertIsInstance(result, list)

    def testAverageIndividual_ReturnsArrayOfDictionariesWithId(self):

        # Act
        result = rank.average_individual()
        first_entry = result[0]

        # Assert
        self.assertTrue('id' in first_entry)

    def testAverageIndividual_ReturnsArrayOfDictionariesWithName(self):

        # Act
        result = rank.average_individual()
        first_entry = result[0]

        # Assert
        self.assertTrue('name' in first_entry)

    def testAverageIndividual_ReturnsArrayOfDictionariesWithCharacter(self):

        # Act
        result = rank.average_individual()
        first_entry = result[0]

        # Assert
        self.assertTrue('character' in first_entry)

    def testAverageIndividual_ReturnsArrayOfDictionariesWithAverage(self):

        # Act
        result = rank.average_individual()
        first_entry = result[0]

        # Assert
        self.assertTrue('average' in first_entry)

    def testAverageIndividual_ReturnsArrayOfDictionariesSortedByAverage(self):

        # Act
        result = rank.average_individual()
        first_entry = result[0]
        second_entry = result[1]

        # Assert
        self.assertGreaterEqual(first_entry.get('average'), second_entry.get('average'))


def main():
    unittest.main()


if __name__ == '__main__':
    main()