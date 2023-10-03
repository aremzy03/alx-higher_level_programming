#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    count = -1
    for i in str:
        count += 1
        if count == n:
            continue
        new_str += i
    return new_str
