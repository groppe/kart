#!/usr/bin/python3.6
import os
import json
import kartlogic.rank
import prettytable

def rank_individuals_by_average_score(event, context):

    # retrieve the ranking board data
    boardData = kartlogic.rank.average_individual()

    # initialize the text table
    table = prettytable.PrettyTable(['Rank', 'Player', 'Character', 'Average'])

    # add player data to table
    for index, player in enumerate(boardData):
        table.add_row([(index + 1), player['name'], player['character'], player['average']])

    # convert the entire table to a string
    table_string = '```' + table.get_string(border=True) + '```'

    # the response body that Slack expects
    slackResponse = {
        'response_type': 'in_channel',
        'text': table_string
    }

    # lambda response
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(slackResponse)
    }

    return response
