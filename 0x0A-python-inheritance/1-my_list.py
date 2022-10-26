#!/usr/bin/python3
"""contains a class MyList that inherits from list"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """Print the list in ascending order"""

        print(sorted(self))
