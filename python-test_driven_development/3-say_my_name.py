#!/usr/bin/python3
"""
This module contains a function that prints a person's full name
in the format 'My name is <first_name> <last_name>'.

The function checks that the inputs are strings and raises a TypeError
if they are not.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If either 'first_name' or 'last_name' are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
