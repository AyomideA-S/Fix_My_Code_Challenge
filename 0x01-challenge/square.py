#!/usr/bin/python3
""" Square class """

class Square():

    """ This is the Square class with 2 variables: width & height """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializer """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Function to find the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ This is the printing function for the Square class """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
