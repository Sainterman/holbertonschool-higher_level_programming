#!/usr/bin/python3
""" create an object from a JSON file """

import json


def load_from_json_file(filename):
    """ open, load file and retrn object """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
