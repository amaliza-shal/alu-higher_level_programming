#!/usr/bin/python3
class Rectangle:
    # Public class attributes
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        # Private instance attributes
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    # Property and setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Property and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Public instance methods
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # String representation using print_symbol
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    # Representation for recreating the instance with eval()
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # Called when an instance is deleted
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # Static method: Returns the biggest rectangle based on area
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    # Class method: Creates a square
    @classmethod
    def square(cls, size=0):
        return cls(size, size)

