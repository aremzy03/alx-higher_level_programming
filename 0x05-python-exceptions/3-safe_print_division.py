#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers
    Args:
        a (int): First integer
        b (int): Second integer
    """
    try:
        result = a / b
    except (ZeroDivisionError, ValueError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
