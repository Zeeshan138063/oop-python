"""
Association:
Its a relationship between two classes and that relationship is established through their objects.
Each object has its own life cycle and there is no owner object. It is a weak type of relationship.
It can be one-to-one, one-to-many, many-to-one, or many-to-many.

For example students and teachers, both classes are associated with each other.
The objects of each class have their own life cycle and there is no owner.
"""

"""
Association:

Association lines are typically drawn as a simple line connecting two classes.
To represent cardinality:
A solid line with a number "1" at one end indicates a one-to-one relationship.
A solid line with a number "N" at one end indicates a one-to-many relationship.
A line with "1" at one end and "N" at the other indicates a many-to-many relationship.
 
 
"""


# Association
class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name
