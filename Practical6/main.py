import os
import pickle
import zipfile
from input import input_students, input_courses, input_marks
from student import Student
from course import Course

# File paths
PICKLED_FILE = "students.dat"

def decompress_files():
    if os.path.exists(PICKLED_FILE):
        print("Decompressing data...")
        try:
            with zipfile.ZipFile(PICKLED_FILE, "r") as zf:
                zf.extractall()
            print("Decompression successful.")
        except Exception as e:
            print(f"Error during decompression: {e}")
    else:
        print(f"{PICKLED_FILE} does not exist. Starting fresh.")

def compress_files():
    print("Compressing data...")
    try:
        with zipfile.ZipFile(PICKLED_FILE, "w") as zf:
            zf.write("data.pkl")
        print("Compression successful.")
        os.remove("data.pkl")  # Clean up uncompressed file
    except Exception as e:
        print(f"Error during compression: {e}")


def load_data():
    if os.path.exists("data.pkl"):
        print("Loading data...")
        try:
            with open("data.pkl", "rb") as f:
                data = pickle.load(f)
            print("Data loaded.")
            return data.get("students", []), data.get("courses", [])
        except Exception as e:
            print(f"Error loading data: {e}")
    else:
        print("No data file found. Starting fresh.")
        return [], []


def save_data(students, courses):
    print("Saving data...")
    try:
        data = {"students": students, "courses": courses}
        with open("data.pkl", "wb") as f:
            pickle.dump(data, f)
        print("Data saved.")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    decompress_files()
    students, courses = load_data()
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
