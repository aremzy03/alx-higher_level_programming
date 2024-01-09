#!/usr/bin/python3
import json
"""writes an object to a text file using
json representation
"""


def save_to_json_file(my_obj, filename=""):
    """writes an object to a text file using
    json representation

    Args:
        my_obj (object): the object file to be converted
        filename (str, optional): the file to be to opened. Defaults to "".
    """
    json_format = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        new_file = file.write(json_format)
