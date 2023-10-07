#!/usr/bin/python3
def no_c(my_string):
    no_c = ""
    for char in my_string:
        if char == "c" or char == "C":
            continue
        else:
            no_c += char
    return no_c
