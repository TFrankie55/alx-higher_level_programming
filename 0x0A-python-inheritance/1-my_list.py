#!/usr/bin/python3
"""Defines an inherited list class Mylist"""


class Mylist(list):
    """Sorts printing for the built-in list class"""

    def print_sorted(self):
        """prints a list in sorted ascending order"""
        print(sorted(self))
