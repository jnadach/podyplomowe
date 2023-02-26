numbers = []
counter = 0

while True:
    if counter > 4:
        break
    try:
        n = int(input("Podaj liczbę załkowitą: "))
        numbers.append(n)
        counter += 1
    except:
        print("To nie jest liczba całkowita. Spróbuj ponownie.")

print(numbers)
