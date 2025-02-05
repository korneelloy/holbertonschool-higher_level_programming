#!/usr/bin/env python3

"""
module for learnig duck typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Shape abstract class
    """
    @abstractmethod
    def area(self):
        """
        area abstract method
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        perimeter abstract method
        """
        pass


class Circle(Shape):
    def __init__(self, radius):
        """
        init method for circle
        """
        self.radius = radius

    def area(self):
        """
        area method for circle
        """
        ar = math.pi * self.radius ** 2
        return ("Area: {}".format(ar))

    def perimeter(self):
        """
        perimeter method for circle
        """
        per = 2 * math.pi * self.radius
        return ("Perimeter: {}".format(per))


class Rectangle(Shape):
    def __init__(self, width, height):
        """
        init method for rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        area methof for rectangle
        """
        ar = self.width * self.height
        return ("Area: {}".format(ar))

    def perimeter(self):
        """
        perimeter method for rectangle
        """
        per = 2 * (self.width + self.height)
        return ("Perimeter: {}".format(per))


def shape_info(any_shape):
    """
    shape_info function via ducktyping
    testing:
    >>> circle = Circle(radius=5)
    >>> shape_info(circle)
    Area: 78.53981633974483
    Perimeter: 31.41592653589793

    >>> rectangle = Rectangle(width=4, height=7)
    >>> shape_info(rectangle)
    Area: 28
    Perimeter: 22
    """
    print(any_shape.area())
    print(any_shape.perimeter())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
