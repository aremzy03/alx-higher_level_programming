#!/usr/bin/python3
"""
This module prints "My name is first_name last_name"
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints "My name is first_name last_name"

    Args:
        first_name (str): the user's first name
        last_name (str, optional): the users last name. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
