#!/usr/bin/python3
"""
The 6-square module defines a class named square
and calcultates its area
prints in #
and uses poitioning
"""


class Square:
    """
    definition of class square with:
    args:
        size (positif int): size of the square
        position:
    method (public):
        returning square area
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) and isinstance(value[0], int) and
           isinstance(value[1], int) and value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        function returning the area of the square
        args:
            self : the square
        """
        return (self.size * self.size)

    def my_print(self):
        """
        prints the square to the standard outout suinf #
        args:
            self: the square (and its size)
        """

        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                if self.position[1] >= 0:
                    print(" " * self.position[0], end="")
                print("#" * self.size)
