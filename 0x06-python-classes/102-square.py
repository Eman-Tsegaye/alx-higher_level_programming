#!/usr/bin/python3

'''This module contains a class named Square'''


class Square:

    '''This Class has an attribute named size'''

    def __init__(self, size=0):
        '''This method initializes this class and sets size'''
        self.__size = size

    def area(self):
        '''This method calculates and returns the area of a square'''
        return (self.__size ** 2)

    @property
    def size(self):
        '''A getter method'''
        return self.__size

    @size.setter
    def size(self, value):
        '''A setter method'''
        if (type(value) != int):
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def __eq__(self, another):
        """Define the == comparision operator to a square"""
        return self.area() == another.area()

    def __ne__(self, another):
        """Define the != comparision operator to a square"""
        return self.area() != another.area()

    def __lt__(self, another):
        """Define the < comparision operator to a square"""
        return self.area() < another.area()

    def __gt__(self, another):
        """Define the > comparision operator to a square"""
        return self.area() > another.area()

    def __le__(self, another):
        """Define the <= comparision operator to a square"""
        return self.area() <= another.area()

    def __ge__(self, another):
        """Define the >= comparision operator to a square"""
        return self.area() >= another.area()
