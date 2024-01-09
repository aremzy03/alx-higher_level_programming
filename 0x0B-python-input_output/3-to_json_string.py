#!/usr/bin/python3
import json
"""
this program returns the json representation
of an object string
"""


def to_json_string(my_obj):
    """Returns the json representation of an
    object string

    Args:
        my_obj (dict): the object to be checked
    """
    return json.dumps(my_obj)
