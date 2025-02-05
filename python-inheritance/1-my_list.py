#!/usr/bin/python3
"""
Module 1-my_list
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """
    Classe MyList that inherits from list
    """

    def print_sorted(self):
        """
        Displays the sorted list in ascending numbers

        This metthod doesn't modify the original list
        """
        print(sorted(self))
