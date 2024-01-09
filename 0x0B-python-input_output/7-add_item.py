#!/usr/bin/python3
import json
import sys
"""
this program adds all the arguements to a lists and
saves them to file
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

        return new_file


def load_from_json_file(filename):
    """This function reads a json file and converts it to
    an object representation

    Args:
        filename (string): the file to be opened
    """
    with open(filename, "r+", encoding="utf=8") as f:
        myobject = f.read()

    return json.loads(myobject)


itemlist = []
try:
    itemlist = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        itemlist.append(sys.argv[i])
    save_to_json_file(itemlist, "add_item.json")
except FileNotFoundError:
    for i in range(1, len(sys.argv)):
        itemlist.append(sys.argv[i])
    save_to_json_file(itemlist, "add_item.json")
