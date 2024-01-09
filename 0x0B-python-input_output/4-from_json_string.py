#!/usr/bin/python3
import json
"""
this program returns the an object (python data structure)
represented by the json format
"""


def from_json_string(my_str):
    """returns an object represented by the json format

    Args:
        my_str (str): the json string to be converted
    """
    return json.loads(my_str)
