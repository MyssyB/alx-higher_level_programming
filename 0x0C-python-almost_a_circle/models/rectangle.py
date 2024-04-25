#!/usr/bin/python3

from base import Base

"""Sub class"""
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Getter for width"""
    def get_width(self):
        return self.__width

    """setter for width"""

    def set_width(self, width):
        self.__width = width

    """Getter for height"""
    def get_height(self):
        return self.__height

    """Setter for height"""
    def set_height(self, height):
        self.__height = height

    """getter for x"""
    def get_x(self):
        return self.__x

    """setter for x"""
    def set_x(self, x):
        self.__x = x

    """getter of y"""
    def get_y(self):
        return self.__y

    """setter for y"""
    def set_y(self, y):
        self.__y = y

