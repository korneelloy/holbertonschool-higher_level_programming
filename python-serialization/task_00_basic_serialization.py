#!/usr/bin/env python3

"""
Basic serialization module that adds the functionality to
serialize a Python dictionary to a JSON file
and deserialize the JSON file to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serialize and save to file
    argv:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
        If the output file already exists it should be replaced.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    load and deserialize
    argv:
        filename: input JSON file
    returns: Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r') as file:
        return json.load(file)
