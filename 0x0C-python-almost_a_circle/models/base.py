#!/usr/bin/python3
"""class Base declaration"""

import json
from os import path

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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + ".json", encoding='utf-8', mode='w') as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                dict_objs = []
                for obj in list_objs:
                    dict_objs.append(cls.to_dictionary(obj))
                jfile.write(cls.to_json_string(dict_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """g'old comment here"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """y know what i mean"""
        if not path.isfile(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", encoding='utf-8', mode='r') as file:
            djson = file.read()
            ljson = []
            for el in cls.from_json_string(djson):
                ljson.append(cls.create(**el))
            return ljson
