#!/usr/bin/python3
"""
    This program opens a file and reads it
"""


def read_file(filename=""):
    """This function opens a file and reads it

    Args:
        filename (str, optional): The file to be open and read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
