#!/usr/bin/python3
"""This module defines a function add_integer(a, b=98) that adds two integers (or floats).

If a and b are floats, they are casted to integers before performing the addition.
"""

def add_integer(a, b=98):
    """Adds two integers (or floats) and returns the result as an integer.
    
    Arguments:
    a -- the first integer or float
    b -- the second integer or float (default is 98)

    Returns:
    The sum of a and b, as an integer.
    
    Raises:
    TypeError -- if a or b is not an integer or float
    """
    
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
