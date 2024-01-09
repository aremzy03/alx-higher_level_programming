#!/usr/bin/python3
"""this program appends a file
"""


def append_write(filename="", text=""):
    """writes a file at the end

    Args:
        filename (str, optional): the file name to be read. Defaults to "".
        text (str, optional): the content to be appended. Defaults to "".
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append = f.write(text)
