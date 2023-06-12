#!/usr/bin/python3
"""module that defines a rectangle that inherits from baseGeometry"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """define rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle object"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """computes and returns the area of the rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """returns string representation of a Rectangle"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
