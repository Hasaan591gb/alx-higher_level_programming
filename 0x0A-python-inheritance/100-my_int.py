#!/usr/bin/python3
"""module that defines a class MyInt based on int"""


class MyInt(int):
    """object like int except equality is reversed"""

    def __eq__(self, value):
        """magic method that inverts == opeartor with !="""

        return self.real != value

    def __ne__(self, value):
        """magic method that inverts != operator with =="""

        return self.real == value
