#!/usr/bin/python3
"""Implementation of Rectangle class which inherits from Base class"""
from models.base import Base
"""importing"""

class Rectangle(Base):
    """Represents a rectangle.

    Attributes:
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        id (int): The identifier of the rectangle. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method for new instance from rectangle class"""
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.y = y
        self.x = x

    @property
    def width(self):
        """ width of the rectangle.
        
        Returns:
            int: width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the rectangle width .

        Args:
            value (int): The desired width value.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the rectangle height.

        Returns:
            int: The rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height.

        Args:
            value (int): The desired height value.

        Raises:
            ValueError: If value is less than 0.
            TypeError: If value is not an integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
   
    @property
    def x(self):
        """Get x as the rectangle's coordinate in X-axis.

        Returns:
            int: The value of X."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x as the rectangle's coordinate in X-axis.

        Args:
            value (int): The value of X.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
 
    @property
    def y(self):
        """Get Y as the rectangle's coordinate in Y-axis.

        Returns:
            int: The value of Y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set Y as the rectangle's coordinate in Y-axis.

        Args:
            value (int): The value of Y..

        Raises:
            ValueError: If value is less than 0.
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """Calculate the area of the rectangle and return it."""
        return self.width * self.height

    def display(self):
        """Display the rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update attributes of the rectangle"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)