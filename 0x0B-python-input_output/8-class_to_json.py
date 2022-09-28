#!/usr/bin/python3

"""function that returns the dictionary"""


def class_to_json(obj):
    """Returns dictionary with a simple data structure."""
    return obj.__dict__
