from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


s = Square(5)
print("Perimeter of Square:", s.perimeter())

r = Rectangle(6, 4)
print("Perimeter of Rectangle:", r.perimeter())