#!/usr/bin/python3
"""
This function divides a rix
"""


def matrix_divided(matrix, div):
    """_summary_

    Args:
        rix (_type_): _description_
        div (_type_): _description_
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
    for item in matrix:
        if isinstance(item, list):
            for num in item:
                if not (isinstance(num, int) or isinstance(num, float)):
                    raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
        else:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    nmatrix = [[round(num / div, 2) for num in row] for row in matrix]
    return nmatrix
