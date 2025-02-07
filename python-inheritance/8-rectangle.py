#!/usr/bin/python3
"""
The base_geometry module for now only creates empty class
with one empty method calculating the area, supposedly
and one method for data validation
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
The rectangle module defines a rectangle
"""


class Rectangle(BaseGeometry):
    """
    the Rectangle class
    """
    def __init__(self, width, height):
        """ init method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
