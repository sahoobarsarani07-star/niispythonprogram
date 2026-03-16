from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class Square(Shape):

    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s * self.s


r = Rectangle(5, 7)
print("Rectangle Area:", r.area())

s = Square(4)
print("Square Area:", s.area())