#!/usr/bin/python3
def uppercase(str):
    string = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            char = ord(c) - 32
            string = string + chr(char)
        else:
            string = string + c
    print("{}".format(string))
