#!/usr/bin/python3
"""
The inherits module verifies
if the object inherits form specified class or subclass
"""


def inherits_from(obj, a_class):
    """
    function verifying if object inherits from class or subclass
    argv:
        obj: the object
        a_class: the class you want to verify against
    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
