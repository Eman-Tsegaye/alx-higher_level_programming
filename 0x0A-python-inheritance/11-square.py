#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square class"""

    def __init__(self, size):
        """Initialization of a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
