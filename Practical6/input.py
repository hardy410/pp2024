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
        marks[student_id] = round(mark, 1)
    return marks
