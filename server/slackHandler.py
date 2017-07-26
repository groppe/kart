#!/usr/bin/python3.6
import os
import json
import logging
import requests
import mario
import plotly
import plotly.plotly as pltly
import plotly.figure_factory as figure_factory
import prettytable

def bigboard(event, context):

    # retrieve the ranking board data
    boardData = mario.bigboard()

    # initialize the text table
    table = prettytable.PrettyTable(['Player', 'Character', 'Average'])

    # add player data to table
    for player in boardData:
        table.add_row([player['name'], player['character'], player['average']])

    # convert the table to a string
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

def bigboard_image(event, context):

    # retrieve the ranking board data
    boardData = mario.bigboard()

    matrix = [['Player', 'Character', 'Average']]

    for player in boardData:
        matrix.append([player['name'], player['character'], player['average']])

    # sign in to plotly
    pltly.sign_in(os.environ.get('PLOTLY_USERNAME'), os.environ.get('PLOTLY_API_KEY'))
    
    # create ranking table
    table = figure_factory.create_table(matrix, colorscale=[[0, '#ff0000'],[.5, '#ffe5e5'],[1, '#ffffff']])

    # change table font size
    for i in range(len(table.layout.annotations)):
        table.layout.annotations[i].font.size = 20

    # plot the table
    result = pltly.plot(table, filename='bigboard')

    # the response body that Slack expects
    slackResponse = {
        'response_type': 'in_channel',
        'attachments': [
            {
                'title': 'Kart Ranking',
                'image_url': result + '.png'
            }
        ]
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
