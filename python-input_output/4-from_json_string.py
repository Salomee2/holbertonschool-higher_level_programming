#!/usr/bin/python3
"""
This module has a function to turn a JSON string into a Python object
"""

import json  # We need this to work with JSON


def from_json_string(my_str):
    """
    Turns a JSON string into a Python object
    """
    return json.loads(my_str)
