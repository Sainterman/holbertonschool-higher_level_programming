#!/usr/bin/python3
"""class Base declaration"""

import json


class Base:
    """This class will be the base of all other classes in project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Assign obj id"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        elif id <= 0:
            raise ValueError("id must be positive integer")
        else:
            self.id = id
            Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string rep of for instances of dicts"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)
