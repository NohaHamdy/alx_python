#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""
class baseGeo(type):
    """The custom meta class"""
    def __dir__(cls):
        """override dir() method for meta class"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass = baseGeo):
    """BaseGeometry class with the custom metaclass"""
    pass

    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']