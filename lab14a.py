#Autor: Jan Nadachowski

PHONES = {
    "Tomek": 342354650,
    "Ada": 345234321,
    "Karol": 965876590,
    "Jan": 453295043
}


def find_telephone_number():
    name = input("Podaj imie: ")
    if PHONES.get(name):
        return PHONES.get(name)
    else:
        return "Nie ma takiej osoby na liście telefonów"


print(find_telephone_number())
