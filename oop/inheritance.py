"""
6. Inheritance:
Inheritance allows you to create a new class that inherits attributes and methods from an existing class.
It's achieved by specifying the parent class in the subclass definition:

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):

    def bark(self):
        print(f"{self.name} is barking")


d = Dog("dog")
d.bark()
d.sleep()
