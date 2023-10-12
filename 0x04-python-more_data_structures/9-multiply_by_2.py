#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    def multiply(x): return x * 2
    n_dictionary = \
        {key: multiply(value) for key, value in a_dictionary.items()}
    return n_dictionary
