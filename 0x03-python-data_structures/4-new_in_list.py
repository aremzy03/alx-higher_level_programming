#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = 0
    n_list = []
    for item in my_list:
        if count == idx:
            n_list.append(element)
        else:
            n_list.append(item)
        count += 1
    return n_list
