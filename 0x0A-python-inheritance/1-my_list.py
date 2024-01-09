#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initialize object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
