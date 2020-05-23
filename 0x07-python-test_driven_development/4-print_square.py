#!/usr/bin/python3
def print_square(size):
    """
    Print a square with the character #

    Args:
        size (int): Size of the square

    Return:
        nothing just prints

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#"*size, end="")
        print()
