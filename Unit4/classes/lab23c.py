#Jan Nadachowski
# Zaprojektuj klasę produktu sklepu internetowego wg wytycznych:
# • stwórz klasę o nazwie Product,
# • dodaj (prywatne) właściwości jak nazwa, kategoria, cena, rabat w procentach,
# • dodaj metodę obliczającą cenę uwzględniającą rabat,
# • dodaj metodę sprawdzającą przynależność produktu do danej kategorii,
# • dodaj metodę reprezentującą obiekt klasy jako ciąg znaków.
# Dodatkowo stwórz grupę produktów z kilku kategorii, ustaw rabat dla produktów z jednej
# kategorii i wyświetl listę produktów.

class Product:
    def __init__(self, name, category, price, discount_perc):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__discount_perc = discount_perc

    def get_dicount_price(self):
        return self.__price * ((100 - self.__discount_perc) / 100)

    def set_dicount_price(self, discount_perc):
        self.__discount_perc = discount_perc

    def get_category(self):
        return self.__category

    def __str__(self):
        return f"Produkt: {self.__name}, " \
               f"kategoria: {self.__category}, " \
               f"cena: {self.__price}zł, " \
               f"rabat: {self.__discount_perc}%, " \
               f"cena po rabacie: {self.get_dicount_price()}zł"


p1 = Product("mleko", "nabiał", 8, 0)
p2 = Product("ser żółty", "nabiał", 7, 0)
p3 = Product("ser biały", "nabiał", 10, 0)
p4 = Product("jajka", "nabiał", 12, 0)
nabial = [p1, p2, p3, p4]

p5 = Product("kiełbasa", "mięso", 32, 0)
p6 = Product("szynka", "mięso", 40, 0)
p7 = Product("kabanos", "mięso", 21, 0)
mieso = [p5, p6, p7]

p8 = Product("pomidor", "warzywa", 9, 0)
p9 = Product("ogórek", "warzywa", 7, 0)
p10 = Product("cukinia", "warzywa", 7, 0)
warzywa = [p8, p9, p10]

products = [nabial, mieso, warzywa]

print("-" * 100)
print("Produkty przed promocją:")
for category in products:
    print()
    for item in category:
        print(item)
print()
print("-" * 100)
print("Produkty z aktywną promocją na warzywa wysokości 25%:")
for i in products[0]:
    i.set_dicount_price(25)
for category in products:
    print()
    for item in category:
        print(item)
print()
