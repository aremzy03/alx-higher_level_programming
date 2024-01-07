#!/usr/bin/python3
"""
This module indents a string
"""


def text_indentation(text):
    """
    The ``text_indentation()`` takes a text as an arguement then indents it at
    the point where a ., ?, and : delimiter is found

    Args:
        text (str): the text to be taken as arguement
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    index = 0
    while index < len(text):
        if text[index] == "." or text[index] == "?" or text[index] == ":":
            print(text[index], end="")
            print("\n")
            index += 2
            continue
        print(text[index], end="")
        index += 1
