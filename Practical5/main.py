import os
import zipfile
from input import input_students, input_courses, input_marks
from student import Student
from course import Course

# File paths
STUDENT_FILE = "students.txt"
COURSE_FILE = "courses.txt"
MARKS_FILE = "marks.txt"
COMPRESSED_FILE = "students.dat"

# Decompress files if the compressed data exists
def decompress_files():
    if os.path.exists(COMPRESSED_FILE):
        print("Decompressing data...")
        try:
            with zipfile.ZipFile(COMPRESSED_FILE, "r") as zf:
                zf.extractall()
            print("Decompression successful.")
        except Exception as e:
            print(f"Error during decompression: {e}")
    else:
        print(f"{COMPRESSED_FILE} does not exist. Starting fresh.")

# Compress files before exiting the program
def compress_files():
    print("Compressing data...")
    try:
        with zipfile.ZipFile(COMPRESSED_FILE, "w") as zf:
            for file in [STUDENT_FILE, COURSE_FILE, MARKS_FILE]:
                if os.path.exists(file):
                    zf.write(file)
        print("Compression successful.")
    except Exception as e:
        print(f"Error during compression: {e}")

# Load data from text files
def load_data():
    students = []
    courses = []
    marks = {}

    # Load students
    if os.path.exists(STUDENT_FILE):
        print("Loading students data...")
        try:
            with open(STUDENT_FILE, "r") as f:
                for line in f:
                    student_id, name, dob = line.strip().split(",")
                    students.append(Student(student_id, name, dob))
            print("Students data loaded.")
        except Exception as e:
            print(f"Error reading {STUDENT_FILE}: {e}")
    
    # Load courses
    if os.path.exists(COURSE_FILE):
        print("Loading courses data...")
        try:
            with open(COURSE_FILE, "r") as f:
                for line in f:
                    course_id, name, credits = line.strip().split(",")
                    courses.append(Course(course_id, name, int(credits)))
            print("Courses data loaded.")
        except Exception as e:
            print(f"Error reading {COURSE_FILE}: {e}")
    
    # Load marks
    if os.path.exists(MARKS_FILE):
        print("Loading marks data...")
        try:
            with open(MARKS_FILE, "r") as f:
                for line in f:
                    course_id, student_id, mark = line.strip().split(",")
                    if course_id not in marks:
                        marks[course_id] = {}
                    marks[course_id][student_id] = float(mark)
            print("Marks data loaded.")
        except Exception as e:
            print(f"Error reading {MARKS_FILE}: {e}")
    
    # Update courses with marks
    for course in courses:
        if course._id in marks:
            course._marks = marks[course._id]

    return students, courses

# Save data to text files
def save_data(students, courses):
    print("Saving data...")
    try:
        # Save students
        with open(STUDENT_FILE, "w") as f:
            for student in students:
                f.write(f"{student._id},{student._name},{student._dob}\n")
        
        # Save courses
        with open(COURSE_FILE, "w") as f:
            for course in courses:
                f.write(f"{course._id},{course._name},{course._credits}\n")
        
        # Save marks
        with open(MARKS_FILE, "w") as f:
            for course in courses:
                for student_id, mark in course.get_marks().items():
                    f.write(f"{course._id},{student_id},{mark}\n")
        print("Data saved.")
    except Exception as e:
        print(f"Error during saving data: {e}")

def main():
    # Decompress existing data
    decompress_files()

    # Load data from files
    students, courses = load_data()

    # Check if data exists; if not, prompt for input
    if not students:
        print("No student data found. Please input student information.")
        students = [Student(*s) for s in input_students()]
    if not courses:
        print("No course data found. Please input course information.")
        courses = [Course(*c) for c in input_courses()]

    while True:
        print("\nMenu:")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks")
        print("4. Calculate GPA")
        print("5. Save and Exit")
        
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
            save_data(students, courses)
            compress_files()
            print("Data saved and compressed. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
