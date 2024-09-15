# -*- coding: utf-8 -*-
"""akshon3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yYiRuYrd_4cQ3CnD6EHdQvSDPCt3YUc6
"""

#Q1
def diff(num):
    if num > 17:
        return 2 * abs(num - 17)
    else:
        return 17 - num

num = int(input("Enter a number: "))
result = diff(num)
print("The result is:", result)

def check(num):
    if num >= 100 and num <= 1000 or num == 2000:
        return 1
    else:
        return 0

num = int(input("Enter a number: "))
result = check(num)
if result == 1:
    print(f"{num} is within the range 100 to 1000 or it is 2000.")
else:
    print(f"{num} is not within the range 100 to 1000 or 2000.")

#Q3
def rev_string(s):
    return s[::-1]

string = input("Enter a string: ")
rev_string = rev_string(string)
print(f"The reversed string is: {rev_string}")

#Q4
def count(string):
    upper = 0
    lower = 0

    for letter in string:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    return upper, lower

string = input("Enter a string: ")
upper, lower = count(string)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

#Q5
def NewList(num):
    return list(set(num))

List = [2,4,6,8,10,100,63,34]
distinctlist = NewList(List)

print("Original list:", List)
print("List with distinct elements:", distinctlist)

def even(List):
    even = [num for num in List if num % 2 == 0]
    return even
List = [10,9,8,7,6,5,4,3,2,1]
result = even(List)

print(f"Even numbers: {result}")

#Q7
def outer(text):
    def inner():
        print(f"Hello {text}")

    inner()

outer("World")

#Q8
def student(Name, Age, Grade):
    student.Name = Name
    student.Age = Age
    student.Grade = Grade

    for attribute in student.__dict__:
        print(f"{attribute} : {getattr(student, attribute)}")

student("akshon",19,"2nd year")

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None

    def set_student_class(self, student_class):
        self.student_class = student_class

    def display_attributes(self):

        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")


student1 = Student(66, "akshon")
student1.set_student_class(" 2nd Year")
student1.display_attributes()

#Q10
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

student1 = Student(1, "akshon", "Second Year")
student2 = Student(2, "hlol", "Fourth Year")

#student1
print("Attributes of student 1:")
student1.display_attributes()
print()

#student2
print("Attributes of student 2:")
student2.display_attributes()

#11
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(3)

print(f"Area of the circle: {circle.area()}")
print(f"Perimeter of the circle: {circle.perimeter()}")

#12
class string_in_upper_case:
    def __init__(self):
        self.text = ""

    def get_String(self):
        self.text = input("Enter a string: ")

    def print_String(self):
        print(self.text.upper())

string_in_upper_case = string_in_upper_case()
string_in_upper_case.get_String()
string_in_upper_case.print_String()