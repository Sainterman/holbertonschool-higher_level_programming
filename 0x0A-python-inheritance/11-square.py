#!/usr/bin/python3
""" we call that a joint """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class uses size """

    def __init__(self, size):
        """ instantiate with size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ RETURN SQUARE OF SIZE """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
