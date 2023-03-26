#Author: Jan Nadachowski
#Napisz klasę zliczającą wszystkie powstałe swoje instancje.

class CountingClass:
    counter = 1

    def __init__(self):
        CountingClass.counter += 1

    def get_counter(self):
        return CountingClass.counter


for i in range(100):
    obj = CountingClass()

print("Liczba instancji klasy CountingClass:", obj.get_counter())

