#!/usr/bin/python3
"""A module for square"""


class Square:
    """This is a square class.

    This class represents a square shape and provides functionality for
    working with squares. It includes an attribute for size and ensures
    that the size is a non-negative integer.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size=0): The constructor for the Square class.
    """
    def __init__(self, size=0):
        """Initialize a Square instance with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
