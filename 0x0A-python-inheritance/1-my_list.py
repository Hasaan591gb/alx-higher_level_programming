#!/usr/bin/python3
"""
    This module defines a class that inherits from list
"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """method that uses sorted function to print
        sorted list"""
        print(sorted(self))
