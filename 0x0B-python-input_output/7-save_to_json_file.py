#!/usr/bin/python3
""" save object to a file """

import json


def save_to_json_file(my_obj, filename):
    """ dump saves to file """
    with open(filename, encoding='utf-8', mode='w') as f:
        json.dump(my_obj, f)
