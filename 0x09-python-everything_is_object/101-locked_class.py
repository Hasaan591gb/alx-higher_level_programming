#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """A class that prevents the user from dynamically
    creating new instance attributes, except if the new
    instance attribute is called `first_name`.

    Attributes:
        first_name: A string representing the first
        name of an instance."""

    __slots__ = ['first_name']
