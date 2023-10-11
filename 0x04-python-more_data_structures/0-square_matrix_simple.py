#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = []
    for list1 in matrix:
        list2 = map(lambda x: x ** 2, list1)
        newm.append(list(list2))
    return newm
