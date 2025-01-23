#!/usr/bin/python3

"""
The say_my_name module handles printing a first and last name
This is handled through the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a first and last name
    Args:
        first_name: first name
        last_name: last name
    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
