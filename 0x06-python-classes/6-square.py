#!/usr/bin/python3
"""A module for square"""


class Square:
    """This is a square class that provides functionality for
    working with squares.

    This class represents a square shape and includes a constructor
    for initializing a square with a specific size
    and an optional position. It provides a property for accessing and
    setting the size of the square,
    and a method to calculate the area of the square. Additionally,
    it includes a method to print a square pattern.

    Attributes:
        _Square__size (int): The size of the square.
        _Square__pos (tuple of int): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Constructor to create
        a square with a specific size and position.
        area(self): Calculate and return the area of the square.
        my_print(self): Print a square pattern using '#' characters
        and a specified position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance with a given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple of int, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not
            a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self._Square__size = size
        self._Square__pos = position

    @property
    def size(self):
        """int: Get or set the size of the square.

        The size attribute represents the side length of the square.
        You can access it using this property or set it to a new value.

        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        return self._Square__size

    def position(self):
        """tuple of int: Get or set the position of the square.

        The position attribute represents the coordinates (x, y)
        of the top-left corner of the square.
        You can access it using this property or set it to a new
        tuple of 2 positive integers.

        Raises:
            TypeError: If the new position is not a tuple
            of 2 positive integers.
        """
        return self._Square__pos

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple of int): The new position for the square.

        Raises:
            TypeError: If the new position is not a tuple of
            2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__pos = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square, which is the square of its size.
        """
        return self._Square__size ** 2

    def my_print(self):
        """Print a square pattern of the specified size and position.

        The square pattern is printed using '#'
        characters with a specified position.

        Example:
            If the square size is 3 and the position is (2, 1), it will print:
              ###
             ###
            ###
        """
        if self._Square__size == 0:
            for a in range(self._Square__pos):
                print(" ")
            print("")
        else:
            for i in range(self._Square__size):
                for k in range(self._Square__pos[0]):
                    print(" ", end="")
                for j in range(self._Square__size):
                    print("#", end="")
                print("")
