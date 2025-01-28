#!/usr/bin/python3
"""
The rectangle module defines an rectangle with width and height
"""


class Rectangle:
    """
    defenition of class rectangle
    argv:
        width (positif int): width of rectangle
        height (positif int): height of rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """
    returns the rectangle's area
    """
    def area(self):
        return self.width * self.height

    """
    returns the rectangle's perimeter
    """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    """
    defines the special string method
    so the string area gets printed with the print_symbol
    if you call print (with or without str) on the rectangle object
    """
    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        else:
            for i in range(self.height - 1):
                for j in range(self.width):
                    string += str((self.print_symbol))
                string += '\n'
            string += str(self.print_symbol) * self.width
            return string

    """
    defines the special repr method
    a string representation of the rectangle
    to be able to recreate a new instance by using eval()
    """
    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    """
    defines the special del method
    for cleanup
    """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """
    returns the biggest of the 2 rectangles
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1
