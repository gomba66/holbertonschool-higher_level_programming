#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(tuple) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for t in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for t2 in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
