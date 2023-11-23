#!/usr/bin/python3
"""
multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """Returns the sum of two matrices

    Args:
        m_a (list): the first matrix as an argument
        m_b (list): the second matrix as the second argument
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) < 1:
        raise ValueError("m_a can't be empty")
    if len(m_b) < 1:
        raise ValueError("m_b can't be empty")
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
        if len(m_a[i]) < 1:
            raise ValueError("m_a can't be empty")
        if i != len(m_a) - 1:
            if len(m_a[i]) != len(m_a[i + 1]):
                raise TypeError("each row of m_a must be of the same size")
        for a in m_a[i]:
            if not isinstance(a, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")
        if len(m_b[i]) < 1:
            raise ValueError("m_b can't be empty")
        if i != len(m_b) - 1:
            if len(m_b[i]) != len(m_b[i + 1]):
                raise TypeError("each row of m_b must be of the same size")
        for b in m_b[i]:
            if not isinstance(b, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(len(m_b)):
                value += m_a[i][k] * m_b[k][j]
            row.append(value)
        result.append(row)
    return result
