#!/usr/bin/python3
# 1-square.py by Hasaan Ahmad
"""defines a square"""


class Square:
    """Represents a square shape."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size
