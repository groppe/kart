#!/usr/bin/python2.7
import kartlogic.rank
import prettytable
import util.web as webutil
import util.slack as slackutil


def handler(event, context):
    input_data = slackutil.parse_input(event['body'])

    if slackutil.validate_slack_token(input_data) is False:
        return webutil.respond_unauthorized("Invalid Slack token")

    return webutil.respond_success("Successful")


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
    slack_response = slackutil.in_channel_response(table_string)

    return webutil.respond_success_json(slack_response)
