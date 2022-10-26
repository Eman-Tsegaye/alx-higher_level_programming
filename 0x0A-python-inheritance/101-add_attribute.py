#!/usr/bin/python3
"""contains a function that adds a new attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
