def main():
    shapes = []
    shapes.append(Rectangle(5,3))
    shapes.append(Triangle(5,2))

    for shape in shapes:
        print(shape)
        print(shape.area())
        print(shape.perimeter())


