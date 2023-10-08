#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        sum1, sum2 = 0, 0
    else:
        if len(tuple_a) > 0 and len(tuple_b) > 0:
            sum1 = tuple_a[0] + tuple_b[0]
        elif len(tuple_a) == 0:
            sum1 = 0 + tuple_b[0]
        elif len(tuple_b) == 0:
            sum1 = tuple_a[0] + 0
        if len(tuple_a) < 2:
            sum2 = 0 + tuple_b[1]
        elif len(tuple_b) < 2:
            sum2 = 0 + tuple_a[1]
        elif len(tuple_a) < 2 and len(tuple_b) < 2:
            sum2 = 0
        else:
            sum2 = tuple_a[1] + tuple_b[1]
    tup1 = (sum1, sum2)
    return tup1
