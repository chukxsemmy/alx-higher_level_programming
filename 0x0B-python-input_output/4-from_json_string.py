#!/usr/bin/python3

"""Defines a JSON - object function."""
import json


def from_json_string(my_str):
    """Returns a Python object representation of a JSON string."""
    return json.loads(my_str)
