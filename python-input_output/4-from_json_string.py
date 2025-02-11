#!/usr/bin/python3

"""json to string module"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by JSON string"""
    return (json.loads(my_str))
