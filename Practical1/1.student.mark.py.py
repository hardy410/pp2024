

def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return (student_id, name, dob)

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (course_id, name)

def input_marks_for_course(students, course_id):
    marks = {}
    print(f"Enter marks for course: {course_id}")
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} (ID: {student[0]}): "))
        marks[student[0]] = mark
    return marks

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(course_id, marks):
    if course_id not in marks:
        print("No marks found for this course.")
        return
    print(f"Marks for course {course_id}:")
    for student_id, mark in marks[course_id].items():
        print(f"Student ID: {student_id}, Mark: {mark}")

def main():
    students = []
    courses = []
    marks = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        students.append(input_student_info())
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        courses.append(input_course_info())

    for course in courses:
        course_id = course[0]
        marks[course_id] = input_marks_for_course(students, course_id)

    while True:
        print("\nMenu:")
        print("1. List courses")
        print("2. List students")
        print("3. Show student marks for a given course")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_courses(courses)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            course_id = input("Enter course ID to view marks: ")
            show_student_marks(course_id, marks)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
