class Student():
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade
    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

student_1 = Student(
    "Serhii",
    "Perederiiev",
    29,
    80
)
print(f'{student_1.name}, {student_1.surname}, {student_1.age}, {student_1.average_grade}')

student_1.change_average_grade(100)

print(f'{student_1.name}, {student_1.surname}, {student_1.age}, {student_1.average_grade}')
