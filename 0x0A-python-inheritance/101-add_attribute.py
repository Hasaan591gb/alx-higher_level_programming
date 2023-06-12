#!/usr/bin/python3
"""module that defines a function to add attributes to objects"""


def add_attribute(obj, att, value):
    """adds a new attribute to given object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
