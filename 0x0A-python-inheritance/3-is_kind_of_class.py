#!/usr/bin/python3
""" Module define kind of class for obj """


def is_kind_of_class(obj, a_class):
    """ determine if obj is instance of a_class
        or inherit from
     """

    if isinstance(obj, a_class):
        return True
    else:
        return False
