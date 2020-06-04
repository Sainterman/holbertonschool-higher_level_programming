#!/usr/bin/python3

"""search and append
"""


def append_after(filename="", search_string="", new_string=""):
    """
    open, search, append
    """
    temportal = ""
    with open(filename, mode='r', encoding="UTF8") as file:
        for j in file:
            if search_string in j:
                temportal += j[:] + new_string
            else:
                temportal += j[:]
    with open(filename, mode='w', encoding="UTF8") as file:
        file.write(temportal)
