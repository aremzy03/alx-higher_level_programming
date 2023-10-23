#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """_summary_

    Args:
        my_list (list, optional): _description_. Defaults to [].
        x (int, optional): _description_. Defaults to 0.
    """
    count = -1
    while count != x:
        try:
            count += 1
            print(my_list[count], end="")
        except Exception:
            break
    print()
    return (count)
