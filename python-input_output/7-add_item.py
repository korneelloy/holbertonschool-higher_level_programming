#!/usr/bin/python3

"""adds all arguments to a Python list, and then save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
try:
    json_object = load_from_json_file(filename)
except FileNotFoundError:
    json_object = []
for arg in sys.argv[1:]:
    json_object.append(arg)
save_to_json_file(json_object, filename)
