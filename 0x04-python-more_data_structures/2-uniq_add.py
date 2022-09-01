#!/usr/bin/python3

def uniq_add(my_list=[]):

    add_uq_int = 0
    for i in set(my_list):
        add_uq_int += i
    return add_uq_int
