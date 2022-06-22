#!/usr/bin/python3


class Square:
    """Class to represent a square."""

    def __init__(self, size=0):
        """Initialize a new square."""
        self.size = size
    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
