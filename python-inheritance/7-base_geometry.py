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
    def __init__(self):
        pass

    """
    method calculating the area
    """
    def area(self):
        raise Exception("area() is not implemented")

    """
    method validating data
    argv:
        name: the name of the attribute
        value: the value of the attribute
    """

    def integer_validator(self, name, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
