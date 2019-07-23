class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    def display_count(self):
        print('Total number of students: %d' % Student.count)

    def display_student(self):
        print('Name:', self.name, 'Age:', self.age)


student1 = Student('Bob', 24)
student2 = Student('Max', 25)

student1.display_count()
student2.display_student()

print("Student.__doc__", Student.__doc__)
print("Student.__name__", Student.__name__)
print("Student.__module__", Student.__module__)
print("Student.__bases__", Student.__bases__)
print("Student.__dict__", Student.__dict__)


class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):
        print('Employee count: %d' % Employee.empCount)

    def display_employee(self):
        print('Name:', self.name, 'Salary:', self.salary)


emp = Employee('Rob', 34)
emp.display_count()
emp.display_employee()
