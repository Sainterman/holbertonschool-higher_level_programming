#!/usr/bin/python3
""" define class Student """


class Student():
    """
    Attributes:
        public instance:
            first_name (string)
            last_name (string)
            age (int)
    """

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """ initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ only attributes from attr and class """

        attributes = dict()
        if type(attrs) is list:
            for attribute, val in self.__dict__.items():
                if attribute in attrs:
                    attributes[attribute] = val
            return attributes
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance
        for the json obj
        """

        if not json:
            return
        self.__dict__ = json
