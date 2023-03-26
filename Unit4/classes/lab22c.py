#Author: Jan Nadachowski
# Napisz klasę reprezentującą obiekty typu książka, w tym celu:
# • stwórz klasę Book z odpowiednimi właściwościami i metodami,
# • stwórz kilka przykładowych egzemplarzy tej klasy,
# • zademonstruj działanie wybranych metod na przykładowych egzemplarzach.

class Book:
    def __init__(self, title, author, publish_date, price):
        self.__title = title
        self.__author = author
        self.__publish_date = publish_date
        self.__price = price
        self.__discount = False
        self.__discount_value = 0

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publish_date(self):
        return self.__publish_date

    def get_price(self):
        return self.__price

    def is_discount(self):
        return self.__discount

    def make_discount(self, discount):
        if discount == 0:
            self.__discount = False
        else:
            self.__discount = True

        self.__price *= 1 - discount
        self.__discount_value = discount

    def show_discount_value(self):
        return str(self.__discount_value * 100) + "%"


def show_discount_books():
    count = 0
    for book in books:
        if book.is_discount():
            print("Książka", book.get_title(), "jest przeceniona o", book.show_discount_value(),
                  ". Cena promocyjna", round(book.get_price(), 1), "zł.")
            count += 1
    if count == 0:
        print("Obecnie nie ma książek na promocji.")


books = []
books.append(Book("Ostatnie życzenie", "Andrzej Sapkowski", 1994, 35))
books.append(Book("Harry Potter i Kamień Filozoficzny", "J. K. Rowling", 1998, 45))
books.append(Book("Python for Everybody", "Charles Russell Severance", 2010, 52))

show_discount_books()

print()
print("Wszystkie książki powyżej 40zł przecenione o 10%")
for book in books:
    if book.get_price() > 40:
        book.make_discount(0.1)
print()

show_discount_books()
