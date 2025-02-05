#!/usr/bin/python3
"""
Module 0-lookup
This module contains a function that gives the list of
attributes and methodes of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methodes available

    Args:
         obj: the object from who we want to get the attributes and methods

    Returns:
            list of attributs and methods from obj
    """
    return dir(obj)
