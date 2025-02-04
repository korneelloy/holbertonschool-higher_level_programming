#!/usr/bin/python3
"""
The base_geometry module for now only creates empty class
with one empty method calculating the area, supposedly
and one method for data validation
"""


class BaseGeometry:
    """
    empty BaseGeometry class
    """
    def area(self):
        """
        method calculating the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method validating data
        argv:
            name: the name of the attribute
            value: the value of the attribute
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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

    def area(self):
        """
        method calculating the area
        """
        return (self.__width * self.__height)

    def __str__(self):
        return (f"[{type(self).__name__}] {str(self.__width)}/{str(self.__height)}")