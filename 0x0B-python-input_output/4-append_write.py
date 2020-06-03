#!/usr/bin/python3
""" define append_write that adds text at end of file """


def append_write(filename="", text=""):
    """  """
    with open(filename, encoding='utf-8', mode='a') as f:
        return(f.write(text))
