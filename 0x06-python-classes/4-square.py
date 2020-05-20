#!/usr/bin/python3
""" class Square that defines a square AND validates size """


class Square:
    """ Square with size verification
    Attributes:
        __size (int): Must be Integer type and >= 0
   """
    __size = 0

    def __init__(self, size=0):
        """ Instantiate with setter """
        self.size = size

    @property
    def size(self):
        """ get size """
        return self.__size

    @size.setter
    def size(self, value):
        """ set proper size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the square """
        return (self.__size * self.__size)
