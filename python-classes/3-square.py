#!/usr/bin/python3
"""
    Why a getter and setter?
    Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
    Using the @property decorators 
"""
    """This code defines a class Square that defines Private instance attribute size

    Raises:
        TypeError: _size must be an integer_
        ValueError: _size must be >= 0_

    Returns:
        _size_: _the size of the square_
    """
class Square:
    """
    Using init function inside the class
    """
    def __init__(self, size=0):
        """
        Initializes the square with the given size
        """
        self.size = size
    """
    Why a getter and setter?
    Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
    """    
    @property
    def size(self):
        """
        Returns the size of the square.

        :return: The size of the square.
        :rtype: int
        """
        retuen self.__size
    
    @size.setter
        
    def size(self, value):
         """
        Sets the size of the square.

        :param value: The new size of the square.
        :type value: int
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

        :return: The area of the square.
        :rtype: int
        """
        return self.__size ** 2