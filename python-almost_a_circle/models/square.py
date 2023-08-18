#!/usr/bin/python3
"""Implementation of Square class which inherits from Rectangle"""
from models.rectangle import Rectangle
"""Importing from Ractangle module"""

class Square(Rectangle):
    """ square class.
    
    Attributes:
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The identifier of the square.
        size (int): The size of the square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance from square.

        Args:
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            size (int): The size of the square.
            id (int): The identifier of the square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the square size.

        Returns:
            int: The square size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the square size.

        Args:
            value (int): The square size value.

        Raises:
            ValueError: If value is under or equals 0.
            TypeError: If value is not an integer."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"