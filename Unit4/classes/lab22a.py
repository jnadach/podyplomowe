# Author: Jan Nadachowski
# Rozbuduj klasę Employee o mechanizm zwiększania wynagrodzeń:
# • dodaj metodę risesalary(),
# • metoda powinna zwiększać zarobki o podaną wartość procentową,
# • domyślnie metoda powinną zwiększać zarobkio 10%.

class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def getsalary(self):
        return self.__salary

    def getfullname(self):
        return self.__firstname + " " + self.__lastname

    def getage(self):
        return self.__age

    def risesalary(self, rise=0.1):
        self.__salary *= 1 + rise


def print_employees(employees):
    for e in employees:
        print(e.getfullname(), "wiek:", e.getage(), "lat, pensja:", e.getsalary(), "zł.")
    print()


employees = []

employees.append(Employee("Jan", "Kowalski", 24, 3800))
employees.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employees.append(Employee("Natalia", "Nowak", 60, 15200))

print("Płace przed podwyżką:")
print_employees(employees)

print("Płace po domyślnej podwyżką 10%:")
for e in employees:
    e.risesalary()
print_employees(employees)

print("Płace po zdefiniowanej podwyżce 20%:")
for e in employees:
    e.risesalary(0.2)
print_employees(employees)
