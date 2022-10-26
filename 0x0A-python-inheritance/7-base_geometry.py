#!/usr/bin/python3
"""contains a class named BaseGeometry"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """raises an Exception"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """function that checks value be positive or not"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
