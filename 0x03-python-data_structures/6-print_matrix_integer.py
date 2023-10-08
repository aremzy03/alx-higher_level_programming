#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list) and len(matrix) != 0:
        for item in matrix:
            if isinstance(item, list) and len(item) != 0:
                count = 1
                for i in item:
                    if count == len(item):
                        print("{:d}".format(i))
                    else:
                        print("{:d} ".format(i), end="")
                    count += 1
    else:
        return
