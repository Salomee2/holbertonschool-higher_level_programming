#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """Serialize the data and save it as a JSON file."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
        

def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file."""
    with open(filename, 'r') as json_file:
        return json.load(json_file)
