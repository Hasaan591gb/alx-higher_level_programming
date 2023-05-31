#!/usr/bin/python3
# 6-square.py by Hasaan Ahmad
"""defines a square"""


class Square:
    """Represents a square shape."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with a given size.

        :param size: The size of the square. Default value is 0.
        :type size: int
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """

        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square to a given value.

        :param value: The new size of the square.
        :type value: int
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than 0.
        """

        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the position of the object.

        Returns:
        tuple: A tuple of two integers representing the position of the object.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the object.

        Args:
        value (tuple): A tuple of two integers
                       representing the new position of the object.

        Raises:
        TypeError: If value is not a tuple of two positive integers.
        """

        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        :return: The area of the square.
        :rtype: int
        """

        return self.__size * self.__size

    def str_print(self):
        """returns the string to print"""
        my_str = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            my_str += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                my_str += " "
            for j in range(self.size):
                my_str += "#"
            my_str += "\n"
        return my_str

    def my_print(self):
        """print the square in position"""
        print(self.str_print(), end='')
