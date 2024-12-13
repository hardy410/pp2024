# pw4/input.py
import math

def input_students():
    students = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append((student_id, name, dob))
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        courses.append((course_id, name, credits))
    return courses

def input_marks(course_name, students):
    marks = {}
    print(f"Enter marks for course: {course_name}")
    for student_id, student_name, _ in students:
        mark = float(input(f"Enter mark for {student_name} (ID: {student_id}): "))
        marks[student_id] = math.floor(mark * 10) / 10
    return marks

# pw4/output.py
import curses

def display_menu(screen, options):
    while True:
        screen.clear()
        for i, option in enumerate(options, 1):
            screen.addstr(f"{i}. {option}\n")
        screen.addstr("Choose an option: ")
        choice = screen.getstr().decode()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)

# pw4/domains/student.py
class Student:
    def __init__(self, student_id, name, dob):
        self._id = student_id
        self._name = name
        self._dob = dob
        self._gpa = 0

    def set_gpa(self, gpa):
        self._gpa = gpa

    def get_gpa(self):
        return self._gpa

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}, GPA: {self._gpa:.1f}"

# pw4/domains/course.py
class Course:
    def __init__(self, course_id, name, credits):
        self._id = course_id
        self._name = name
        self._credits = credits
        self._marks = {}

    def input_marks(self, students):
        self._marks = input_marks(self._name, students)

    def get_marks(self):
        return self._marks

    def get_credits(self):
        return self._credits

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Credits: {self._credits}"

# pw4/main.py
import curses
from pw4.input import input_students, input_courses
from pw4.output import display_menu
from pw4.domains.student import Student
from pw4.domains.course import Course

def main(screen):
    students = [Student(*s) for s in input_students()]
    courses = [Course(*c) for c in input_courses()]

    while True:
        choice = display_menu(screen, ["List students", "List courses", "Input marks", "Exit"])

        if choice == 1:
            screen.clear()
            screen.addstr("Students:\n")
            for student in students:
                screen.addstr(str(student) + "\n")
            screen.addstr("Press any key to return to the menu.")
            screen.getch()
        elif choice == 2:
            screen.clear()
            screen.addstr("Courses:\n")
            for course in courses:
                screen.addstr(str(course) + "\n")
            screen.addstr("Press any key to return to the menu.")
            screen.getch()
        elif choice == 3:
            screen.clear()
            screen.addstr("Enter course ID to input marks: ")
            course_id = screen.getstr().decode()
            course = next((c for c in courses if c._id == course_id), None)
            if course:
                course.input_marks([(s._id, s._name, s._dob) for s in students])
            else:
                screen.addstr("Course not found. Press any key to return to the menu.")
                screen.getch()
        elif choice == 4:
            break

if __name__ == "__main__":
    curses.wrapper(main)
