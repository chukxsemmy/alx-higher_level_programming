#!/usr/bin/python3


"""A read function"""


def read_file(filename=""):
    """Function opens a file for.reading"""
    with open(filename, 'r',  encoding="utf-8") as f:
        for i in f:
            print(i, end='')
