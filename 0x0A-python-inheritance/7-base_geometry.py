#!/usr/bin/python3
""" module describes class BaseGeometry """


class BaseGeometry():
    """ empty class """

    def __init__(self):
        """ nothing happens yet """

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
