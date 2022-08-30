#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        ai = 0
        aj = 0
    elif len_a == 1:
        ai = tuple_a[0]
        aj = 0
    else:
        ai = tuple_a[0]
        aj = tuple_a[1]

    if len_b == 0:
        bi = 0
        bj = 0
    elif len_b == 1:
        bi = tuple_b[0]
        bj = 0
    else:
        bi = tuple_b[0]
        bj = tuple_b[1]

    my_matrix = (ai + bi, aj + bj)

    return (my_matrix)
