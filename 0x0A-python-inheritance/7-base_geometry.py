#!/usr/bin/python3
"""Module that defines a class BaseGeometry"""


class BaseGeometry:
    """this class represents a base geometry object"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value if integer"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
