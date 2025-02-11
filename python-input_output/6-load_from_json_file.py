#!/usr/bin/python3

"""json file to object"""

import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, 'r', encoding='UTF-8') as file:
        content = file.read()
    return (json.loads(content))
