# Pobierz od użytkownika trzy liczby całkowite reprezentujące długości odcinków i
# sprawdź czy jest możliwe zbudowanie z tych odcinków trójkąta prostokątnego.
# Jan Nadachowski

l = []

for i in range(3):
    a = int(input("Podaj liczbe: "))
    l.append(a)

print(l)

result = False

counter = 0
while counter < 3:
    if l[0] ** 2 + l[1] ** 2 == l[2] ** 2:
        result = True
        l = [l[1], l[2], l[0]]
    counter += 1

print(result)





