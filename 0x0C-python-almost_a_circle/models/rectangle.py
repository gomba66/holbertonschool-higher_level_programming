#!/usr/bin/python3
""" This module contains a new class called Rectangle """

from models.base import Base


class Rectangle(Base):
    """ This is a class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Inicialize all atributes """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Method width for retrieve the value """

        return self.__width

    @width.setter
    def width(self, value):
        """ Method that sets a value to width """

        self.__width = value

    @property
    def height(self):
        """ Method height for retrieve the value """

        return self.__height

    @height.setter
    def height(self, value):
        """ Method that sets a value to height """

        self.__height = value

    @property
    def x(self):
        """ Method for retrieve the value """

        return self.__x

    @x.setter
    def x(self, value):
        """ Method that sets a value to x """

        self.__x = value

    @property
    def y(self):
        """ Method for retrieve the value """

        return self.__x

    @y.setter
    def y(self, value):
        """ Method that sets a value to y """

        self.__y = value
