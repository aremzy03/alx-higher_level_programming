#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        count = 1
        for i in item:
            if count == len(item):
                print("{}".format(i))
            else:
                print("{} ".format(i), end="")
            count += 1
