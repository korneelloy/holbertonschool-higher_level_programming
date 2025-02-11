#!/usr/bin/python3

"""save in file as json representation"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation:"""
    with open(filename, 'w', encoding='UTF-8') as file:
        json_representation = json.dumps(my_obj)
        file.write(json_representation)
