#!/usr/bin/python3
"""
The is_same_class module verifies
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    function verifying if object is same class
    argv:
        obj: the object
        a_class: the class you want to verify against
    """
    if type(obj) is a_class:
        return True
    else:
        return False
