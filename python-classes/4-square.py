#!/usr/bin/python3
"""
The 4-square module defines a class named square
and calcultates its area
"""


class Square:
    """
    definition of class square with:
    args:
        size (positif int): size of the square
    method (public):
        returning square area
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        function returning the area of the square
        args:
            self : the square
        """
        return (self.size * self.size)
