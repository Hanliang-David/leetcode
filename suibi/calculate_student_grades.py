# calculate_student_grades.py
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        total = sum(student.average_grade() for student in self.students)
        return total / len(self.students)

students = [
    Student("Alice", [85, 92, 88]),
    Student("Bob", [78, 81, 74]),
    Student("Charlie", [93, 87, 91])
]

gradebook = Gradebook()
for student in students:
    gradebook.add_student(student)

print("Student Averages:")
for student in gradebook.students:
    print(f"{student.name}: {student.average_grade():.2f}")

print(f"Class Average: {gradebook.class_average():.2f}")
