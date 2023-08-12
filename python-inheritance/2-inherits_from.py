#!/usr/bin/python3
"""Checks object class"""

def inherits_from(obj, a_class):
    """
    This function checks if a class is instance or what
    
    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to check against.

    Returns:
    bool: True if `obj` is an instance of `a_class`, False otherwise.
    """
    result = isinstance(obj, a_class) and type(obj) != a_class
    return result