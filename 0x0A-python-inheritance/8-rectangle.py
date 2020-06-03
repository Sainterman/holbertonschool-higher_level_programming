#!/usr/bin/python3
""" module describes class BaseGeometry and rectangle """


class BaseGeometry():
    """
    attributes:
        area(): not implemented
        integer_validator(): validates integer values
        width(int): positive integers
    """
    

    def __init__(self, width, height):
        """ nothing bruh """
        pass

    def area(self):
        """ not implemented """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Inherits BaseGeometry class and adds width and height """

    __width = 0
    __height = 0

    def __init__(self, width, height):
        """ instantiate width and height """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
