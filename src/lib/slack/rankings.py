#!/usr/bin/python2.7
import prettytable

import lib.rank as ranking
import lib.slack.util as slackutil
import lib.webutil as webutil


def handle():
    # retrieve the rankings
    rankings = ranking.average_individual()

    # initialize the text table
    table = prettytable.PrettyTable(['Rank', 'Player', 'Character', 'Average'])

    # add each ranking entry to the table
    for index, player in enumerate(rankings):
        table.add_row([(index + 1), player['name'], player['character'], player['average']])

    # covert the table to format that Slack will understand
    table_string = '```' + table.get_string(border=True) + '```'
    slack_response = slackutil.in_channel_response(table_string)

    return webutil.respond_success_json(slack_response)
