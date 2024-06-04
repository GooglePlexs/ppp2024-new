from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class equilateral_Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return 3 * self.base

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class RegularHexagon(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side ** 2

    def perimeter(self):
        return 6 * self.side

def main():
    shapes = []
    shapes.append(Rectangle(5,3))
    shapes.append(equilateral_Triangle(5,2))

    for shape in shapes:
        print(shape)
        print(shape.area())
        print(shape.perimeter())

if __name__ == "__main__":
    main()

# 일반 삼각형의 경우는 어떻게 하지??