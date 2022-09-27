#!/usr/bin/python3
"""returns the JSON representation of an object"""


import json


def to_json_string(my_obj):
    """Returns Jason"""
    new = json.dumps(my_obj)
    return (new)
