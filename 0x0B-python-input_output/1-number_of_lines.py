#!/usr/bin/python3
""" return number of lines in text file """


def number_of_lines(filename=""):
    """ open, count and close """
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
