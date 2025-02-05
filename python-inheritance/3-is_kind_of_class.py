#!/usr/bin/python3
"""
Module containing the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
