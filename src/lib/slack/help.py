#!/usr/bin/python3.6
import lib.common.web as webutil


def handle():
    help_text = '*Usage:* /mario <command>\n*Commands:*\n```'
    help_text += '\n1a. average ranking'
    help_text += '\n1b. skill ranking'
    help_text += '\n2. played <#> games, <user1> <score1>, <user2> <score2>[, <user3> <score3>]'
    help_text += '\n3. characters'
    help_text += '\n4. add character "<character name>" <character image url>'
    help_text += '\n5. add player @<player>'
    help_text += '\n6. my character is "<valid character name>"'
    help_text += '\n7. my name is "<name you want to be called>"'
    help_text += '```'
    return webutil.respond_success(help_text)
