#!/usr/bin/python3
""" Creation of a Square Class """


class Square:
    """ This class will be the blueprint for every square object """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Constructor of the Square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Modification of the way the Obj is printed """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ Main func to create an instance """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
