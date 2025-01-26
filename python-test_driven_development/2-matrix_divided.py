#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix by a given divisor.
The function validates the matrix and the divisor, and returns a new matrix with the 
results, rounded to 2 decimal places.

Exceptions:
- TypeError: If the matrix is not a list of lists of integers/floats or if rows are not 
  the same size.
- TypeError: If 'div' is not a number (integer or float).
- ZeroDivisionError: If 'div' is zero.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by 'div' and returns a new matrix.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by 'div', rounded to 2 decimal places.

    Raises:
        TypeError: If matrix or div is invalid.
        ZeroDivisionError: If div is 0.
    """
    
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows are of the same size
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if all elements are integers or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create a new matrix with the divided and rounded results
    return [[round(element / div, 2) for element in row] for row in matrix]
