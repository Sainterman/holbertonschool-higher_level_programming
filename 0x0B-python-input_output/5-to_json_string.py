#!/usr/bin/python3
""" define function that returns JSON representation of
an object(string)

"""


import json


def to_json_string(my_obj):
    """ return a JSON formated string with my_obj attributes """
    return json.dumps(my_obj)
