#!/usr/bin/python3
"""module that defines class Square based on Rectagle class"""


class Square(__import__('9-rectangle').Rectangle):
    """Defines a square object"""

    def __init__(self, size):
        """Initialize a new square with size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
