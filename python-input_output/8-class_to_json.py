#!/usr/bin/python3

"""
Module that defines a function to convert an object
to a JSON-friendly dict."""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure
    """
    return obj.__dict__
