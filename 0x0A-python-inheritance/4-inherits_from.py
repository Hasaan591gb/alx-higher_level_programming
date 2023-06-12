#!/usr/bin/python3
"""
    module that checks if object is an instance of a class that
    inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """True if object is an instance of a class that inherited
    (directly or indirectly) from the specified class, False otherwise
    """

    return type(obj) != a_class and issubclass(type(obj), a_class)
