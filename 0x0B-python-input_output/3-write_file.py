#!/usr/bin/python3
""" write content into file, creates if non existing with
write_file
"""


def write_file(filename="", text=""):
    """ open in write mode, write text and return amount of bytes written """
    with open(filename, encoding='utf-8', mode='w') as f:
        return(f.write(text))
