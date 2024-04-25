#!/usr/bin/python3

class Base:
    """First class"""

    """Private class attribute"""
    __nb_objects = 0
    
    """class constructor"""
    def __init__(self, id=None):
        self.name = name
        if id is not None:
            self.id = id
        else (__nb_objects++)
            self.id = __nb_objects

