#!/usr/bin/python3
"""
The base_geometry module for now only creates empty class
with one empty method
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
