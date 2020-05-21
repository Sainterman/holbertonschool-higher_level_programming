#!/usr/bin/python3
""" class Square that defines a square AND validates size """


class Square:
    """ Square with size verification
    Attributes:
        __size (int): Must be Integer type and >= 0
   """
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """ Instantiate with setter """
        self.size = size
        self.position = position

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

    def my_print(self):
        """ print a # square """
        if self.size > 0:
            if (self.__position[1] > 0):
                for j in range(self.__position[1]):
                    print()
            for i in range(self.size):
                for jeje in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """ retrieve position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position property """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
