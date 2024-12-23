from input import input_marks

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
