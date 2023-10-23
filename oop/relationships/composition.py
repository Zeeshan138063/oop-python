"""
Composition:
It defines a strong type of relationship. It can be defined as when a class can reference one or more objects of another
 class inside its instance variable. In composition, objects can not exist independently.

We can implement the above example of students and departments in a composition manner.
In this example student object is instantiated inside the department object.
Whenever a department object is destroyed, a student object will automatically destroy.

Composition is defined as Part-of relationship between objects.

In UML, it is denoted by a straight line with a filled arrowhead at one end.
"""


class Student:
    def __init__(self, id):
        self.id = id

    def registration_number(self, department_id):
        return f"{self.id}_{department_id}"


class Department:
    def __init__(self, id, student_id):
        self._id = id
        self._student = Student(student_id)

    def student_registration(self):
        return self._student.registration_number(self._id)


dept = Department(10, 990)
print(dept.student_registration())
