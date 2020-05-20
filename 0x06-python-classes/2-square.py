#!/usr/bin/python3
""" class Square that defines a square AND validates size """


class Square:
    """ Square with size verification
    Attributes:
        __size (int): Must be Integer type and >= 0
   """
    __size = 0

    def __init__(self, size=0):
        """ Instantiate with proper size a Square object """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
