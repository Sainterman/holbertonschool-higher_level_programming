#!/usr/bin/python3
""" Function that returns the dictionary description
 for JSON serialization of an object
"""


def class_to_json(obj):
    """ deserialize obj with loads """
    return obj.__dict__
