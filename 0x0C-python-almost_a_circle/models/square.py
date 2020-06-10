#!/usr/bin/python3

"""Square class declaration
inherits from Rectangle class

"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Child of Rectangle Class
    Args:
    id
    size
    x, y

    """

    def __init__(self, size, x=0, y=0, id=None):
        """init with rectangle constructor
        replace height and width as size
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """private attr size is same as size and height"""
        return self.width

    @size.setter
    def size(self, value):
        """overwrites height and width of instance"""
        self.width = value
        self.height = value

    def __str__(self):
        """Info about size, polsition and id"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        1st argument should be the id attr
        2nd argument should be size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute

        no-keywortd argument

        Must check data type before updating
        setattr not safe for different data type
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)
