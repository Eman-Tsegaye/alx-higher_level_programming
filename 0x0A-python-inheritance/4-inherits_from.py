#!/usr/bin/python3
"""contains the checker function"""


def inherits_from(obj, a_class):
    """Check the object is an instance of a class that inherited from class"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
