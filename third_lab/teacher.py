"""
Базовый класс Person с атрибутами name, age
Дочерний класс Teacher с дополнительными атрибутами:
subject (преподаваемый предмет)
students (список объектов Student)
Реализуйте методы для работы со списком студентов:
add_student()
remove_student()
list_students()
"""
from typing import List
import students

class Person():
    """Person object
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Teacher(Person):
    """Teacher object

    Args:
        Person class: parent class
    """

    def __init__(self, name: str, age: int, subject: str, students: List):
        self.sybject = subject
        self.students = students
    
    def add_student(self, student_name: str, student_id: int, student_grades: List[int]):
        student = students.Student(student_name, student_id, student_grades)
        self.students.append(student)

    def remove_student(self, student_id: int):
        pass

    def list_students(self):
        print(*self.students)

if __name__ == "__main__":
    teacher = Teacher("Иван", 45, "Python", [])
    teacher.add_student("Arsenii")
    