#!/usr/bin/python3
"""Task"""


class Square:
    """This is a class"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square"""
        return self.__size ** 2

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ne__(self, other):
        return self.size != other.size

    def __eq__(self, other):
        return self.size == other.size
