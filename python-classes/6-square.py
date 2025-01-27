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
        printing with #, white space and new lines
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
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
           not isinstance(value[0], int) or not isinstance(value[1], int)
           or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
            self: the square (and its size and position)
        """

        if self.size == 0:
            print()
        else:
            if self.position[1] != 0:
                print("" * self.position[1])
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
