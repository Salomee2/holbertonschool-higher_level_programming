#!/usr/bin/python3
""" module containinf def of a square class"""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialize a square with a private size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2
