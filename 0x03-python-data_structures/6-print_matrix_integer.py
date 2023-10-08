#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        count = 1
        for i in item:
            if count == len(item):
                print("{:d}".format(i))
            else:
                print("{:d}".format(i), end="")
                print(" ", end="")
            count += 1
