#!/usr/bin/python3
"""
The is_kind_of_class module verifies
if the object is an instance of the specified class or subclass
"""


def is_kind_of_class(obj, a_class):
    """
    function verifying if object is same class or subclass
    argv:
        obj: the object
        a_class: the class you want to verify against
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
