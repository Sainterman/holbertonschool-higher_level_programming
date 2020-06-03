#!/usr/bin/python3
""" read files with utf 8 encoding and prnit to stdout """


def read_file(filename=""):
    """ open, read print and close file """
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        print(text)
