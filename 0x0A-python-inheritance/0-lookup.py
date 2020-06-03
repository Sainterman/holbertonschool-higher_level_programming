#!/usr/bin/python3
""" lookuop module """


def lookup(obj):
    """ all attributes and methods of obj """
    return list(dir(obj))
