#!/usr/bin/python3
"""
This module has a function to turn a Python object into a JSON string.
"""

import json  # We need this to work with JSON


def to_json_string(my_obj):
    """
    Changes a Python object into a JSON string.

    JSON is a format that looks like a Python dictionary,
    but its actually just text
    """
    return json.dumps(my_obj)
