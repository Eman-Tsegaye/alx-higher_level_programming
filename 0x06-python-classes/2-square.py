#!/usr/bin/python3

'''This module contains a class named Square'''


class Square:

    '''This Class has an attribute named size'''

    def __init__(self, size=0):
        '''This method initializes this class and sets size'''
        if (type(size) != int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
