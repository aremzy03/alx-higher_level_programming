#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides contents of list 1 by list 2

    Args:
        my_list_1 (_type_): the first list
        my_list_2 (_type_): the second list
        list_length (_type_): length of both list
    """
    new_list = []
    count = 0
    while count != list_length:
        try:
            result = my_list_1[count] / my_list_2[count]
            new_list.append(result)
        except ValueError:
            result = 0
            new_list.append(result)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by zero")
        except IndexError:
            print("out of range")
        count += 1
    return new_list
