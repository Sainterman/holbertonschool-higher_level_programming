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

    def __str__(self):
        """ string representation of the rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            elestring = ""
            for i in range(self.height - 1):
                elestring += ("#"*self.width) + '\n'
            elestring += ("#"*self.width)
            return elestring

    def __repr__(self):
        """ strng representation of class rectangle """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ say byre rectangle """
        print("Bye rectangle...")

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

    def area(self):
        """ returns the rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)
