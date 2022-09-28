#!/usr/bin/python3

"""text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line.
    Args:
        filename (str): file name.
        search_string (str): search for string within the file.
        new_string (str): new string to insert.
    """
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
