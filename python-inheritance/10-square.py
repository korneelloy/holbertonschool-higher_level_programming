#!/usr/bin/python3
"""
The base_geometry module for now only creates empty class
with one empty method calculating the area, supposedly
and one method for data validation
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    the square class
    """
    def __init__(self, size):
        """
        init method
        """
        self.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        """
        method calculating the area
        """
        return (self.__size * self.__size)

    def __str__(self):
        phrase = "[Rectangle] {}/{}"\
            .format(self.__size, self.__size)
        return (phrase)
