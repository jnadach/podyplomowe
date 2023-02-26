while True:
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        print("Odwrotna liczba to", 1 / number)
    except ZeroDivisionError:
        print("Nie wolno dzielić przez zero!")
    except ValueError:
        print("Niepoprawna wartość. Podaj liczbę całkowitą.")
