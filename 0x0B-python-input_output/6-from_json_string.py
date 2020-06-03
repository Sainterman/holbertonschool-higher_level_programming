#!/usr/bin/python3
""" function that returns an object (Python data structure)
 represented by a JSON string: from_json_string
"""
import json


def from_json_string(my_str):
    """ return an object representation decoded from a json string """
    return json.loads(my_str)
