#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """_summary_

    Args:
        my_list (list, optional): _description_. Defaults to [].
        x (int, optional): _description_. Defaults to 0.
    """
    count = 0
    while count != x:
        try:
            print(my_list[count], end="")
            count += 1
        except (IndexError, TypeError):
            break
    print()
    return (count)
