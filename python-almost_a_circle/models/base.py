#!/usr/bin/python3
"""Creating of the base class"""
class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id = None):
        """This is the Init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects