from input import input_students, input_courses, input_marks
from management.student import Student
from management.course import Course

def main():
    students = [Student(*s) for s in input_students()]
    courses = [Course(*c) for c in input_courses()]

    while True:
        print("\nMenu:")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks")
        print("4. Calculate GPA")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nStudents:")
            for student in students:
                print(student)
        elif choice == "2":
            print("\nCourses:")
            for course in courses:
                print(course)
        elif choice == "3":
            course_id = input("Enter course ID to input marks: ")
            course = next((c for c in courses if c._id == course_id), None)
            if course:
                course.input_marks([(s._id, s._name, s._dob) for s in students])
            else:
                print("Course not found.")
        elif choice == "4":
            for student in students:
                total_marks = 0
                total_credits = 0
                for course in courses:
                    marks = course.get_marks()
                    if student._id in marks:
                        total_marks += marks[student._id] * course.get_credits()
                        total_credits += course.get_credits()
                gpa = total_marks / total_credits if total_credits else 0
                student.set_gpa(round(gpa, 1))
            print("\nStudents with GPA:")
            for student in students:
                print(student)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
