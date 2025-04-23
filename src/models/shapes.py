class Shape:
    def draw(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return f"Drawing a Circle with radius {self.radius}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return f"Drawing a Rectangle with width {self.width} and height {self.height}"