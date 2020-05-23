#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places

    Args:
        matrix (list of lists): must be a list of lists
            of integers or floats
        div (int): must be a number (integer or float)

    Returns:

        new (list of lists): new matrix of elements from matrix
        divided by div
    """

    TypeMessage = "matrix must be a matrix (list of lists) of integers/floats"
    RowMessage = "Each row of the matrix must have the same size"
    DivMessage = "div must be a number"

    for lists in matrix:
        if not lists:
            raise TypeError(TypeMessage)

    new = [[] for i in range(len(matrix))]

    if type(div) not in [int, float]:
        raise TypeError(DivMessage)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        rowSize = len(matrix[i])
        if rowSize != len(matrix[0]):
            raise TypeError(RowMessage)
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) in [int, float]:
                new[i].append(round(matrix[i][j] / div, 2))
            else:
                raise TypeError(TypeMessage)
    return new
