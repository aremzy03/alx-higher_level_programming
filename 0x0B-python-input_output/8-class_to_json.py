#!/usr/bin/python3
"""
this programreturns the dictionary description
with simple data structure(list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """returns h=the dictionary description with 
    simple data structure for JSON serialization
    of an object

    Args:
        obj (class): the object to be converted
    """
    return obj.__dict__
