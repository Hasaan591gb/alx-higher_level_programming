#!/usr/bin/python3
"""This is a class that defines a rectangle"""


class Rectangle:
    """A class used to represent a rectangle.

    Attributes
    ----------
    width : int
        The width of the rectangle (default 0).
    height : int
        The height of the rectangle (default 0).

    Methods
    -------
    None"""

    def __init__(self, width=0, height=0):
        """Initializes the width and height of the rectangle.

        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default 0).
        height : int, optional
            The height of the rectangle (default 0)."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns
        -------
        int
            The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters
        ----------
        value : int
            The new width of the rectangle.

        Raises
        ------
        TypeError
            If `value` is not an integer.
        ValueError
            If `value` is negative.
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns
        -------
        int
            The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Parameters
        ----------
        value : int
            The new height of the rectangle.

        Raises
        ------
        TypeError
            If `value` is not an integer.
        ValueError
            If `value` is negative."""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        The area is calculated by multiplying the width
        and height of the rectangle.

        Returns:
            float: The area of the rectangle."""

        return self.__height * self.__width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        If either the width or height of the rectangle is 0,
        the perimeter is 0. Otherwise, the perimeter is calculated
        as twice the sum of the width and height.

        Returns:
            float: The perimeter of the rectangle."""

        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self) -> str:
        """Returns a string representation of a rectangle.

        The rectangle is represented using the '#' character for each cell.
        Rows are separated by a newline character.

        If the width or height of the rectangle is 0,
        an empty string is returned.

        Returns:
            str: The string representation of the rectangle."""

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle.

        The string representation is in the format 'Rectangle(width, height)',
        where 'width' and 'height' are the width and height of the rectangle,
        respectively.

        Returns:
            str: The string representation of the rectangle."""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
