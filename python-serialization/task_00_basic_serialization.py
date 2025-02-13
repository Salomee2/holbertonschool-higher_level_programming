#!/usr/bin/env python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"The data has been serialized and saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving the data: {e}")

def load_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it into
    a Python dictionary
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data has been loaded from '{filename}'.")
        return data
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None
