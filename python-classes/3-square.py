#!/usr/bin/python3


"""
This module defines a Square class that represents a square shape.
"""
class Square:
    """
    A class that represents a square shape.

    Attributes:
        __size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """
        Initializes the square with the given size
        
        Args:
           size(int): The size of the square. 
        """
        self.size = size
   
    """
    Why a getter and setter?
    Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
    Using the @property decorators 
    """
    @property
    def size(self):
        """
        Getter method for the size of the square.

        Returns:
            int: The size of the square.
        """
        retuen self.__size
    
    @size.setter
        
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: _size must be an integer.
            ValueError: _size must be >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0 :
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2