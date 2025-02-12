#!/usr/bin/python3
"""Module defining the Student class with serialization
and deserialization"""


class Student:
    """Student class that defines a student by first_name,
    last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance with the given attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the
        Student instance filtered by the given list of
        attribute names.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value
                    for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """Reloads the student's attributes from a JSON """
        for key, value in json.items():
            setattr(self, key, value)
