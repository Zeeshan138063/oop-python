class Bird:
    def __init__(self, name="Bird"):
        self.name = name

    def __str__(self):
        return self.name


"""
Class attributes in Python are attributes that are associated with a class rather than with an instance of the class.
They are shared among all instances of the class and have the same value for each instance. 
Class attributes are defined at the class level and are accessible through the class itself and all its instances. 
Here's a detailed explanation of class attributes:

"""


class Car:
    # class attributes
    units_sold = 0


"""
Accessing Class Attributes:
You can access class attributes using the class name or an instance of the class.
"""

# print(Car.units_sold)
# c = Car()
# print(c.units_sold)

"""
Modifying Class Attributes:
Class attributes can be modified at the class level, and the change will be reflected in all instances.
"""
# Car.units_sold = 5
# print(Car.units_sold)
# c = Car()
# print(c.units_sold)

"""
When to Use Class Attributes:
Class attributes are useful in various scenarios:

Constants: You can use class attributes to define constants that have the same value for all instances of a class. 
For example, you might use a class attribute to define a constant like PI in a Circle class.

Configuration: If you have configuration settings that should be the same for all instances of a class, 
you can use class attributes to store these settings.

Shared Data: If you have data that is shared among all instances of a class, such as a count of how many instances have 
been created, you can store it as a class attribute.

Default Values: Class attributes can provide default values that instances can use if they don't have their own values 
for a particular attribute.
"""


# Here's an example that illustrates the use of a class attribute as a constant:
class Circle:
    PI = 3.14159  # class attribute

    def __init__(self, radius):
        self.radius = radius

    #  Instance Methods:
    # Instance methods are functions defined within the class, and they typically operate on the instance's attributes.
    # They always have self as their first parameter:
    def calculate_radius(self):
        return 2 * self.radius * self.PI


#
# circle = Circle(5)
# circle2 = Circle(10)
# print(circle.calculate_radius())
# print(circle2.calculate_radius())


# Shared Data: If you have data that is shared among all instances of a class,
# such as a count of how many instances have been created, you can store it as a class attribute.

class Car:
    count_sold = 0

    def __init__(self, name="Alsvin"):
        self.name = name
        Car.count_sold = Car.count_sold + 1

    def __str__(self):
        return f"name: {self.name} total units sold [{self.count_sold}]"  #


# car1=Car("Honda")
# print(car1)
# car2=Car("Toyota")
# print(car2)
# car3=Car()
# print(car3)

"""
class methods and static methods are special types of methods that are defined within a class but are not bound 
to an instance of the class. They can be called on the class itself rather than on an instance of the class. 
Class methods and static methods have different use cases and behavior. 
"""


class MyClass:
    class_variable = 0

    def __init__(self, number):
        self.instace_variable = number

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    def __str__(self):
        return f"class variable {self.class_variable}: instance variable {self.instace_variable}"


obj = MyClass(10)
print(obj)  # class variable 0: instance variable 10

obj2 = MyClass(20)
print(obj2)  # class variable 0: instance variable 20

MyClass.increment_class_variable()

print(obj)  # class variable 1: instance variable 10

print(obj2)  # class variable 1: instance variable 20

"""
Static methods are typically used for utility functions that are related to the class but don't require access
to instance-specific or class-specific attributes. They are bound to the class for organization purposes.
"""


class MyUtils:

    @staticmethod
    def add(x, y):
        return x + y


print(MyUtils.add(7, 9))  # 16

"""
When to Use Class Methods and Static Methods:
Class Methods:

Use class methods when you need to perform operations that are related to the class as a whole.
They are often used for alternative constructors (factory methods) or for modifying class-level attributes.
Class methods can be used to create instances of a class with different initialization procedures.
Static Methods:

Use static methods when you have a utility function that is logically related to the class but doesn't need access to instance-specific or class-specific attributes.
They are often used for simple operations that don't require knowledge of the class or its instances.
Static methods are helpful for code organization, as they make it clear that the method is related to the class.
"""

"""
Encapsulation is one of the four fundamental principles of object-oriented programming (OOP),
 the other three being inheritance, polymorphism, and abstraction.
"""