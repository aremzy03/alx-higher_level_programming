#!/usr/bin/python3
class Square:
    """This is a square class that provides functionality
    for working with squares.

    This class represents a square shape and includes a constructor
    for initializing a square with a specific size.
    It provides a property for accessing and setting the size of the square,
    and a method to calculate the area of the square.

    Attributes:
        _Square__size (int): The size of the square.

    Methods:
        __init__(self, size=0): Constructor to create a square
        with a specific size.
        area(self): Calculate and return the area of the square.
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

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square, which is the square of its size.
        """
        return self._Square__size ** 2
