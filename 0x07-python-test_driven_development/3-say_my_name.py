#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    H - Say my name.
    .... Heisenberg
    H - You're god damn right.

    Args:

    first_name (string): first paert of name

    last_name (string): second part of name

    Return:

    nothing, just prints

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if not last_name:
        print("My name is {:s} ".format(first_name))
        return

    print("My name is {:s} {:s}".format(first_name, last_name))
