#!/usr/bin/python3
""" Module 2-append_write
 contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file
    Args:
        filename: filename
        text: text to write
    Raises
        Exception: when  file can be opened
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
