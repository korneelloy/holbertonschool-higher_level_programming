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
        self.__radius = radius

    def area(self):
        """
        area method for circle
        """
        ar = math.pi * self.__radius ** 2
        print("Area: {}".format(ar))

    def perimeter(self):
        """
        perimeter method for circle
        """
        per = 2 * math.pi * self.__radius
        print("Perimeter: {}".format(per))


class Rectangle(Shape):
    def __init__(self, width, height):
        """
        init method for rectangle
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        area methof for rectangle
        """
        ar = self.__width * self.__height
        print("Area: {}".format(ar))

    def perimeter(self):
        """
        perimeter method for rectangle
        """
        per = self.__width + self.__height
        print("Perimeter: {}".format(2 * (per)))


def shape_info(any_shape):
    """
    shape_info function via ducktyping
    """
    any_shape.area()
    any_shape.perimeter()
