#!/usr/bin/python3
"""module that defines a rectangle that inherits from baseGeometry"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """define rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle object"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
