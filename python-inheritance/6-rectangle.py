#!/usr/bin/python3
"""Definition for an empty class called BaseGeometry."""
class CustomMeta(type):
    """A custom meta class"""
    def __dir__(cls):
        """override dir() method for meta class"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass = CustomMeta):
    """BaseGeometry class with a custom metaclass"""
    
    def integer_validator(self, name, value):
        """Validation for a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
    def area(self):
        """new area funtion"""
        raise Exception("area() is not implemented")

    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class Rectangle(BaseGeometry):
    """inherited from base class"""
    def __init__(self, width, height):
        self.__height = super().integer_validator("height", height)
        self.__width = super().integer_validator("width", width)
        