#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
The rectangle module defines a rectangle
"""


class Rectangle(BaseGeometry):
    """
    the Rectangle class
    """
    def __init__(self, width, height):
        self.integer_validator("py 8", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
