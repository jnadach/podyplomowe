# Autor: Jan Nadachowski
# 1. Stwórz klasę o nazwie Student i utwórz 3 instancje nowo utworzonej klasy

class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


Student1 = Student("Jan")
Student2 = Student("Ewa")
Student3 = Student("Iwo")

print("Student 1 ma na imię:", Student1.get_name())
print("Student 2 ma na imię:", Student2.get_name())
print("Student 3 ma na imię:", Student3.get_name())
