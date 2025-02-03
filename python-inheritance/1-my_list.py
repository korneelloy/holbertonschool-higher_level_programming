#!/usr/bin/python3
"""
The my_list module handles creates a class of type list
and has a sorted print method
"""


class MyList(list):
    """
    defines an object of type list
    """
    def __init__(self):
        pass

    def print_sorted(self):
        new_list = list
        new_list = sorted(self)
        print(new_list)
