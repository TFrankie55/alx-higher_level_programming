#!usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """returns a list of attributes and methods of an obj"""
    return dir(obj)
