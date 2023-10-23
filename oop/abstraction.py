"""
Abstraction is one of the fundamental principles of object-oriented programming (OOP) and plays a crucial role in
organizing and managing complex software systems. It refers to the process of simplifying complex reality by modeling
classes based on the essential properties and behaviors of objects, while hiding the unnecessary details.
In essence, abstraction involves focusing on what an object does (its behavior) and what it is (its attributes),
while ignoring how it achieves those behaviors or how those attributes are implemented.
"""


class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


"""
Abstraction simplifies the process of modeling real-world objects in software, allowing you to focus on the most 
critical aspects while ignoring less important details. It leads to more organized, reusable, and maintainable code.
"""

r = Rectangle("white",2,5)
print(r.area())
c=Circle("red",2)
print(c.area())