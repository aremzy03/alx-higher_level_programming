#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx > len(my_list) -1 or idx < 0:
        return my_list
    n_list = my_list
    n_list[idx] = element
    return n_list
