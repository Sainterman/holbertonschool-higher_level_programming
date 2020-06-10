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

    def __init__(id, size, x=0, y=0):
        """init with rectangle constructor
        replace height and width as size
        """
        super().__init__(id, size, size, x, y)
