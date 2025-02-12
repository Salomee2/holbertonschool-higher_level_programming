#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object as a JSON string in a file.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(my_obj, file)
    except TypeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))


my_list = [1, 2, 3]
save_to_json_file(my_list, "my_list.json")

my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {'age': 36, 'average': 3.14}
}
save_to_json_file(my_dict, "my_dict.json")

try:
    my_set = {132, 3}
    save_to_json_file(my_set, "my_set.json")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
