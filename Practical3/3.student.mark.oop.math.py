# 3.student.mark.oop.math.py
import math
import numpy as np
import curses

class Person:
    def __init__(self, person_id, name, dob):
        self._id = person_id
        self._name = name
        self._dob = dob

    def get_info(self):
        return self._id, self._name, self._dob

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}"

class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name, dob)
        self._gpa = 0

    def set_gpa(self, gpa):
        self._gpa = gpa

    def get_gpa(self):
        return self._gpa

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}, GPA: {self._gpa:.1f}"

class Course:
    def __init__(self, course_id, name, credits):
        self._id = course_id
        self._name = name
        self._credits = credits
        self._marks = {}

    def input_marks(self, students):
        print(f"Enter marks for course: {self._name} (ID: {self._id})")
        for student in students:
            student_id, student_name, _ = student.get_info()
            mark = float(input(f"Enter mark for {student_name} (ID: {student_id}): "))
            mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
            self._marks[student_id] = mark

    def get_marks(self):
        return self._marks

    def get_credits(self):
        return self._credits

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Credits: {self._credits}"

class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            self._students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = int(input("Enter course credits: "))
            self._courses.append(Course(course_id, name, credits))

    def list_students(self):
        print("Students:")
        for student in self._students:
            print(student)

    def list_courses(self):
        print("Courses:")
        for course in self._courses:
            print(course)

    def input_marks_for_course(self):
        course_id = input("Enter course ID to input marks: ")
        course = next((c for c in self._courses if c._id == course_id), None)
        if course:
            course.input_marks(self._students)
        else:
            print("Course not found.")

    def calculate_gpa(self):
        for student in self._students:
            total_weighted_score = 0
            total_credits = 0
            for course in self._courses:
                marks = course.get_marks()
                if student._id in marks:
                    total_weighted_score += marks[student._id] * course.get_credits()
                    total_credits += course.get_credits()
            gpa = total_weighted_score / total_credits if total_credits > 0 else 0
            student.set_gpa(round(gpa, 1))

    def sort_students_by_gpa(self):
        self._students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def display_menu(self, screen):
        while True:
            screen.clear()
            screen.addstr("Student Mark Management System\n")
            screen.addstr("1. List students\n")
            screen.addstr("2. List courses\n")
            screen.addstr("3. Input marks for a course\n")
            screen.addstr("4. Calculate GPA\n")
            screen.addstr("5. Sort students by GPA\n")
            screen.addstr("6. Exit\n")
            screen.addstr("Choose an option: ")
            choice = screen.getstr().decode()

            if choice == "1":
                screen.clear()
                screen.addstr("Students:\n")
                for student in self._students:
                    screen.addstr(str(student) + "\n")
                screen.addstr("Press any key to return to the menu.")
                screen.getch()
            elif choice == "2":
                screen.clear()
                screen.addstr("Courses:\n")
                for course in self._courses:
                    screen.addstr(str(course) + "\n")
                screen.addstr("Press any key to return to the menu.")
                screen.getch()
            elif choice == "3":
                self.input_marks_for_course()
            elif choice == "4":
                self.calculate_gpa()
            elif choice == "5":
                self.sort_students_by_gpa()
            elif choice == "6":
                break
            else:
                screen.addstr("Invalid choice. Press any key to try again.")
                screen.getch()

if __name__ == "__main__":
    smm = StudentMarkManagement()
    smm.input_students()
    smm.input_courses()
    curses.wrapper(smm.display_menu)
