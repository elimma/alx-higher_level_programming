#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lnA = len(tuple_a)
    lnB = len(tuple_b)

    if lnA < 1:
        tuple_a = (0, 0)
    elif lnA < 2:
        tuple_a = (tuple_a[0], 0)
    if lnB < 1:
        tuple_b = (0, 0)
    elif lnB < 2:
        tuple_b = (tuple_b[0], 0)
    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res

