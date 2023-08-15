#!/usr/bin/python3
"""Definition for an empty class called BaseGeometry."""
class CustomMeta(type):
    """A custom meta class"""
    def __dir__(cls):
        """override dir() method for meta class"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass = CustomMeta):
    """BaseGeometry class with a custom metaclass"""
    def area(self):
        """new area funtion"""
        raise Exception("area() is not implemented")

    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']