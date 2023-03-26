# Autor: Jan Nadachowski
# Zaprojektuj klasę reprezentującą osobę (Person) wg założeń:
# • każdy obiekt tej klasy powinien posiadać właściwości: imię oraz wiek,
# • zabezpiecz właściwości obiektu przed przypadkowym nadpisaniem,
# • ustawienie odpowiednich właściwości obiektu powinno następować podczas jego tworzenia,
# • każdy obiekt tej klasy powinien móc wykonać akcję przedstawienia się.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        return f"Mam na imię {self.__name} i mam {self.__age} lat."


osoba = Person("Jan", 39)
print(osoba.introduce())
