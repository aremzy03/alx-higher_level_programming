#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    executes a function

    Args:
        fct (_type_): _description_
    """
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        sys.stderr.write("Exception: {}\n".format(err))
    return result
