#!/usr/bin/python3
""" is same class module """


def is_same_class(obj, a_class):
    """ determine if obj is instance of a_class """

    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
