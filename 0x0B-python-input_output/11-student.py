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

    def to_json(self):
        """ deserialize obj """
        return self.__dict__
