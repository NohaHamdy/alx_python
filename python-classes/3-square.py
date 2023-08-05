#!/usr/bin/python3
"""
    Why size is private attribute?
    The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
"""

class Square:
    """
    Using init function inside the class
    """
    def __init__(self, size=0):
        self.size = size
        
    @property
    def size(self):
        retuen self.__size
        
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0 :
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            
    def area(self):
        return self.__size ** 2