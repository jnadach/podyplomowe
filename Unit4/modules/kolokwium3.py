# Autor Jan Nadachowski
# Napisz skrypt znajdujący wszystkie liczby z przedziału od 100  do 300, które dzielą się jednocześnie przez 5 i 8.

def find_numbers():
    result = []
    for i in range(100, 301):
        if i % 5 == 0 and i % 8 == 0:
            result.append(i)
    return result


print("Liczby z przedziału od 100  do 300, które dzielą się jednocześnie przez 5 i 8 to:\n", find_numbers())
