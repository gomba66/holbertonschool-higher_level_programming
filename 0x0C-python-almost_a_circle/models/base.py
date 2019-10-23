#!/usr/bin/python3
""" This module contains a class called Base. """


class Base:
    """ This is the base class. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Special method that inicialize all atributes """
        if id is None:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = self.__nb_objects
        else:
            self.id = id
