#!/usr/bin/python3
"""Checks object class"""

def is_same_class(obj, a_class):
    """
    This function checks if a class is instance or what
    
    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to check against.

    Returns:
    bool: True if `obj` is an instance of `a_class`, False otherwise.
    """
    result = isinstance(obj, a_class)
    if result:
        return True
    else:
        return False