#!/usr/bin/python3
def safe_print_integer(value):
    """Prints the integers if it doesn't return error

    Args:
        value (_type_): the integer to be printed
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
