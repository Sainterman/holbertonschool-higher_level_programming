#!/usr/bin/python3
"""find peak in a list"""


def find_peak(list_of_integers):
    """return the peak"""
    length = len(list_of_integers)
    if length == 0:
        return None
    kek = sorted(list_of_integers)
    if kek[-1] == list_of_integers[0]:
        return kek[-2]
    return kek[-1]
