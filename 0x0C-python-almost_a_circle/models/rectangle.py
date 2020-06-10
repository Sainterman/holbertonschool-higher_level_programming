#!/usr/bin/python3
"""Rectangle Class declaration"""
from models.base import Base


class Rectangle(Base):
    """
    Child of base class
    Args:
    width, height
    x, y

    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize from Base clas and set private attributes
        width (int)
        height (int)
        x (int, optional): 0 default
        y (int, optional): 0 default
        id ([id]): None default
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """x position getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x coordinate"""
        self.position_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """x position getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """set x coordinate"""
        self.position_validator("y", value)
        self.__y = value

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.size_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.size_validator("height", value)
        self.__height = value

    def area(self):
        """Rectangle area is width * height"""
        return self.width * self.height

    def display(self):
        """ string representation of the rectangle """
        elestring = "\n" * self.y

        for i in range(self.height - 1):
            elestring += " " * self.x
            elestring += ("#"*self.width) + '\n'
        elestring += " " * self.x
        elestring += ("#"*self.width)
        print(elestring)

    def __str__(self):
        """Info about width, height and polsition and id"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        1st argument should be the id attr
        2nd argument should be the width atrr
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute

        no-keywortd argument

        Must check data type before updating
        setattr not safe for different data type
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""
        return self.__dict__

    def size_validator(self, name, value):
        """ validate value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be > 0".format(name))

    def position_validator(self, name, value):
        """validate coordinates value and type"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{:s} must be >= 0".format(name))
