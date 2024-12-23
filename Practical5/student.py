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
