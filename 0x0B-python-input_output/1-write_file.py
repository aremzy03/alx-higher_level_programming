#!/usr/bin/python3
"""
This program writes the file
"""


def write_file(filename="", text=""):
    """writes to a file

    Args:
        filename (str, optional): the file to write to. Defaults to "".
        text (str, optional): contents to be written. Defaults to "".
    """
    with open(filename, 'w', encoding="utf-8") as f:
        file = f.write(text)
