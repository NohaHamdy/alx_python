#!/usr/bin/python3
"""Definition for an empty class called BaseGeometry."""
class BaseGeometry(metaclass=CustomMeta):
    """BaseGeometry class with the custom metaclass"""
    pass

    def __dir__(cls):
        """Overrides dir() method for the class"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class CustomMeta(type):
    """A custom metaclass"""
    def __dir__(cls):
        """Override dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
