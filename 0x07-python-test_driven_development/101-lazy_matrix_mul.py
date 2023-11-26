#!/usr/bin/bash
"""Lazy matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function finds the products between two matrices and returns
    the result

    Args:
        m_a (list): a list of a list acting ad the first argument
        m_b (list): another list of a list acting as the second arguement

    Returns:
        list: returns a new list of a list containing the result
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) < 1:
        raise ValueError("m_a cannot be empty")
    if len(m_b) < 1:
        raise ValueError("m_b cannot be empty")
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of a lists")
        if len(m_a[i]) < 1:
            raise TypeError("m_a cannot be empty")
        if i != len(m_a) - 1:
            if len(m_a[i]) != len(m_a[i + 1]):
                raise TypeError("Each row of m_a must be the same size")
        if i == len(m_a):
            if len(m_a[i]) != len(m_a[i - 1]):
                raise TypeError("Each row of m_a must be the same size")
        for mat in m_a[i]:
            if not isinstance(mat, (float, int)):
                raise TypeError("m_a should only contain integers or floats")
    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of a lists")
        if len(m_b[i]) < 1:
            raise TypeError("m_b cannot be empty")
        if i != len(m_b) - 1:
            if len(m_b[i]) != len(m_b[i + 1]):
                raise TypeError("Each row of m_b must be the same size")
        if i == len(m_b):
            if len(m_b[i]) != len(m_b[i - 1]):
                raise TypeError("Each row of m_b must be the same size")
        for mat in m_b[i]:
            if not isinstance(mat, (float, int)):
                raise TypeError("m_b should only contain integers or floats")
    mat1 = np.array(m_a)
    mat2 = np.array(m_b)
    result = np.dot(mat1, mat2)
    return result
