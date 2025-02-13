#!/usr/bin/env python3

"""
module for serialization and deserialization of python dict to xml
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialization from dict to xml code
    argv:
        dictionary
        filename where to write the xml code
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)

    with open(filename, 'w') as file:
        tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    dserialization from xml to python lib
    argv:
        filename with xml code
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {child.tag: child.text for child in root}

    return dictionary
