#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers in a matrix.
    
    Args:
        matrix (list of lists): 2D array of integers.

    Returns:
        list of lists: New matrix with squared values.
    """
    return [[x ** 2 for x in row] for row in matrix]
