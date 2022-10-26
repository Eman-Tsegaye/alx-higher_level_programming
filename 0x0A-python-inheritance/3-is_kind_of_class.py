#!/usr/bin/python3
"""Contains the checker function"""


def is_kind_of_class(obj, a_class):
    """Check the object is an instance of a class or
    a class that it inherited from
    """

    return isinstance(obj, a_class)
