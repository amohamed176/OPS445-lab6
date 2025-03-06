#!/usr/bin/env python3
# Author ID: amohamed176

class Student:

    # Define the name and student ID number (which is a string) when a student object is created, ex. student1 = Student('john', '025969102')
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    # Display student name and number
    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    # Add a new course and grade to students record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the grade point average of all courses and display it
    def displayGPA(self):
        if not self.courses:
            print('No courses available to calculate GPA.')
            return
        gpa = sum(self.courses.values()) / len(self.courses)
        print(f'GPA of student {self.name} is {gpa:.2f}')
