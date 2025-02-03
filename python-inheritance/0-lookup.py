#!/usr/bin/python3
"""
The lookup module handles information concerning objects and inheritance
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    Args:
        obj: the object you want to obtain information about
    """
    return (dir(obj))
