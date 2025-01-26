def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div."""
    # Vérification que matrix est une liste de listes
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que chaque ligne de la matrice a la même taille
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        
    # Vérification que div est un nombre (int ou float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Vérification que div n'est pas égal à 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Division de chaque élément de la matrice
    return [[round(element / div, 2) for element in row] for row in matrix]

