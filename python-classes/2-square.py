#!/usr/bin/python3
"""
The 2-square module defines an class named square
"""


class Square:
    """
    definition of class square with:
    args:
        size (positif int): size of the square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
