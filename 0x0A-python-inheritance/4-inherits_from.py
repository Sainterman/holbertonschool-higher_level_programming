#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ determine if obj class is instance
    of a class that inherits of a_class
     """

    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
