#!/usr/bin/python3

"""object to json module"""

import json


def to_json_string(my_obj):
    """returns JSON representation of an object (string):"""
    return (json.dumps(my_obj))
