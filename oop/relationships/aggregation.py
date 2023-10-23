"""
Aggregation:
It's a unidirectional association. When an object can access another object then that relationship is called aggregation
Objects can exist independently in this relationship.

We can define it in a more concise way, aggregation is when an object of one class can own or access
the object of another class.

Let's take an example of a student and department.
There are two classes,
one is a student and
the other is a department.
Students are assigned a registration number based on the specific department. Let's implement its code in python.

Aggregation defined by Has-A relationship between objects.
In UML, it is denoted by a straight line with an empty arrowhead at one end.

https://faun.pub/association-aggregation-composition-python-ec9947832cbd
"""


class Student:
    def __init__(self, id):
        self._id = id

    def registration_number(self, department_id):
        return f"##{self._id}_000_{department_id}"

class Department:
    def __init__(self,id, student):
        self._id = id
        self._student = student

    def student_registration(self):
        return self._student.registration_number(self._id)

if __name__ == '__main__':
    student = Student(10)
    department = Department(20, student)
    print(department.student_registration())
