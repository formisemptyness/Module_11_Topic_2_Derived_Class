'''
Program: derived_class.py
Author: Joshua M. McGinley
Last date modified: 11/09/2022

Reviewing why you wanted to learn about derived classes. The Student is a Person relationship.
Take the class Person.

class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy


    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address

Implement derived class Student

    In the constructor
        Add attribute major, default value 'Computer Science'
        Add attribute gpa, default value '0.0'
        Add attribute student_id, not optional
        Consider all private
    Override method display()

Test your code with the following driver:

# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student

OUTPUT:
Song, River:(900111111) Computer Science gpa: 0.0
Song, River:(900111111) Computer Engineering gpa: 0.0
Song, River:(900111111) Computer Engineering gpa: 4.0

How else could you test your derived class? You thought you were done with testing, but there is always testing!
'''

class Person:
    """Person class"""
    def __init__(self, lname, fname):
        self.last_name = lname
        self.first_name = fname

    def display(self):
        return self.last_name + ", " + self.first_name

class Student(Person):
    '''Student derived class of Person'''
    def __init__(self, stu_id, last_name, first_name, maj = 'Computer Science', _gpa = 0.0, ):
        super().__init__(last_name, first_name)
        self.student_id = stu_id
        self.major = maj
        self.gpa = _gpa

    def display(self):
        return self.last_name + ', ' + self.first_name + ':(' + str(self.student_id) + ') ' + self.major + ' gpa: ' + str(self.gpa)

# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student

# Actual Output.
#Song, River:(900111111) Computer Science gpa: 0.0
#Song, River:(900111111) Computer Engineering gpa: 0.0
#Song, River:(900111111) Computer Engineering gpa: 4.0
