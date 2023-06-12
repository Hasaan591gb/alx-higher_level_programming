#!/usr/bin/python3
"""This module checks if given object is an instance of a class
    or if the object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """True if object is an instance of the
    class or if the object is an instance of a class
    that inherited from False otherwise
    """

    return isinstance(obj, a_class)
