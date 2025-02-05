#!/usr/bin/python3
"""
Module containing function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is an instance of a_class

    Args:
        obj: object to test
        a_class: class to compare

    Returns:
        bool: True if obj is an instance of a_class else false
    """
    return type(obj) is a_class
