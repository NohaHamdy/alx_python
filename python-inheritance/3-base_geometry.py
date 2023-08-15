#!/usr/bin/python3
"""Definition for an empty class called BaseGeometry."""
class BaseGeometry(metaclass = baseGeo):
    """BaseGeometry class with the custom metaclass"""
    pass

    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class CustomMeta(type):
    """A custom Meta class"""
    def __dir__(cls):
        """override dir() method for meta class"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']