#!/usr/bin/python3
"""contains MyInt class that inherits from int"""


class MyInt(int):
    """Invert the operators == and !="""

    def __eq__(self, value):
        """change (==) operator to (!=)"""

        return self.real != value

    def __ne__(self, value):
        """change (!=) operator to (==)"""

        return self.real == value
