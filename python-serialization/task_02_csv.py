#!/usr/bin/env python3
"""
module reading data from one format (CSV)
and converting it into another format (JSON)
using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(CSV_filename):
    """
    convert cvs to json
    argv:
        CVS file
    """
    try:
        with open(CSV_filename, mode='r') as file:
            reader = csv.DictReader(file)
            diction = [row for row in reader]
    except FileNotFoundError:
        return False
    with open('data.json', 'w') as file:
        json.dump(diction, file)
        return True
