#!usr/bin/python3
"""checks Same class or Inherited from"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified class"""

    return isinstance(obj, a_class) or isinstance(type(obj), a_class)
