#!/usr/bin/Python3
def safe_print_list_integers(my_list=[], x=0):
    """_summary_

    Args:
        my_list (list, optional): _description_. Defaults to [].
        x (int, optional): _description_. Defaults to 0.
    """
    count = 0
    success = 0
    while count != x:
        try:
            print("{:d}".format(my_list[count]), end="")
            success += 1
        except (ValueError, TypeError):
            pass
        count += 1
    print()
    return success
