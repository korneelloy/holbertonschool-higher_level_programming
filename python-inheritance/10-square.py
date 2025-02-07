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
        super().__init__(size, size)
