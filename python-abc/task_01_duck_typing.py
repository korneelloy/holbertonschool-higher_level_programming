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
        self.radius = abs(radius)

    def area(self):
        """
        area method for circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        perimeter method for circle
        """
        return 2 * math.pi * self.radius


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
        return self.width * self.height

    def perimeter(self):
        """
        perimeter method for rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(any_shape):
    """
    shape_info function via ducktyping
    """
    print("Area: {}".format(any_shape.area()))
    print("Perimeter: {}".format(any_shape.perimeter()))


if __name__ == '__main__':
    circle = Circle(radius=5)
    shape_info(circle)

    rectangle = Rectangle(width=4, height=7)
    shape_info(rectangle)
