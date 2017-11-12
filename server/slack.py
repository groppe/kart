#!/usr/bin/python2.7
import kartlogic.rank
import util.web
import util.slack
import prettytable
import logging
import json


def post(event, context):
    logging.warning(json.dumps(event))
    return util.web.lambda_response_success("Successful")


def rank_individuals_by_average_score(event, context):
    # retrieve the ranking board data
    board_data = kartlogic.rank.average_individual()

    # initialize the text table
    table = prettytable.PrettyTable(['Rank', 'Player', 'Character', 'Average'])

    # add player data to table
    for index, player in enumerate(board_data):
        table.add_row([(index + 1), player['name'], player['character'], player['average']])

    # convert the entire table to a string
    table_string = '```' + table.get_string(border=True) + '```'

    # the response body that Slack expects
    slack_response = util.slack.in_channel_response(table_string)

    return util.web.lambda_response_success_json(slack_response)
