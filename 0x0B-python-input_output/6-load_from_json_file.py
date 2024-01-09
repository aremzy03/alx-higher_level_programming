#!/usr/bin/python3
import json
"""this program creates an object from an json file
"""


def load_from_json_file(filename):
    """This function reads a json file and converts it to
    an object representation

    Args:
        filename (string): the file to be opened
    """
    with open(filename, "r", encoding="utf=8") as f:
        myobject = f.read()

    return json.loads(myobject)
