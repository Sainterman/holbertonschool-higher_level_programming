#!/usr/bin/python3
""" module describes class rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits BaseGeometry class and adds width and height """

    def __init__(self, width, height):
        """ instantiate width and height """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
