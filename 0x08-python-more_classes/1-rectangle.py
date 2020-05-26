#!/usr/bin/python3
""" Define a class rectangle """


class Rectangle:
    """
    Rectangle class

    Attributes:
        __width (int): private argument for the size of a rectangle
        __height (int): private argument to create a rectangle
    """
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ initializer for a rectangle object.

            Args:
                width (int): initial horizontal size of rectangle
                height (int): initial vertical size of rectangle
            width and height are optional
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set proper width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set proper height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
