def main():
    shapes = []
    shapes.append(Rectangle(5,3))
    shapes.append(Triangle(5,2))

    for shape in shapes:
        print(shape)
        print(shape.area())
        print(shape.perimeter())

from abc import ABC, abstractmethod class Shape(ABC):
@abstractmethod def area(self):
pass
@abstractmethod def perimeter(self):
pass
class Rectangle(Shape): def __init__(self, h, v):
class Triangle(Shape): def __init__(self, h, v):

class Circle(Shape): def __init__(self, r):
class RegularHexagon(Shape):
def __init__(self, r):
