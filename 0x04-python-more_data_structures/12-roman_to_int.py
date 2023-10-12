#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_val = 0
    for ch in roman_string[::-1]:
        val = my_dict[ch]
        if val < prev_val:
            num -= val
        else:
            num += val
        prev_val = val
    return num
