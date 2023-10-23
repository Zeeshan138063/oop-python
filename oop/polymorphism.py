"""
Polymorphism is another important concept of object-oriented programming. It simply means more than one form.

That is, the same entity (method or operator or object) can perform different operations in different scenarios.

Polymorphism  can be achieved in two main ways in OOP: method overriding (with inheritance) and method overloading.

Method Overriding (Dynamic Polymorphism):
This is the most common form of polymorphism and involves a subclass providing a specific implementation of a method
that is already defined in its superclass.
The overridden method in the subclass has the same name, return type, and parameters as the method in the parent class.

Method Overloading (Static Polymorphism):
Method overloading allows a class to have multiple methods with the same name but different parameter lists.
The correct method to execute is determined at compile-time based on the number and types of arguments passed to it.



Let's see an example,
"""
"""
Method Overriding (Dynamic Polymorphism):
Method overriding allows a subclass to provide a specific implementation for a method defined in its superclass. 
The overridden method has the same name, return type, and parameters as the method in the parent class. 
This allows you to call the method on objects of the subclass as if they were objects of the superclass.
"""

class Polygon:
    def render(self):
        print("Polygon rendering")


class Square(Polygon):
    def render(self):
        print("Square rendering")


class Circle(Polygon):
    def render(self):
        print("Circle rendering")


p = Polygon()
p.render()  # Polygon rendering
s = Square()
s.render()  # Square rendering

c = Circle()
c.render()  # Circle rendering

# In this example, the Polygon class defines a method render, and the Square and Circle subclasses override this method
# to provide specific implementations. The render method is called on objects of the Square and Circle classes,
# and the correct implementation is used based on the actual type of the object, demonstrating polymorphism.
"""
Polymorphism allows you to work with objects at a higher level of abstraction, making it easier to design and maintain
 code, and it's a powerful tool for building flexible and extensible software.
"""