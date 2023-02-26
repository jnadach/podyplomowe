# Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
# Uwzględnij możliwość pomyłki użytkownika.

result = []
counter = 1
while counter < 4:
    try:
        number = float(input("Podaj liczbę: "))
        result.append(number)
        counter += 1
    except:
        print("Podano błędną wartość. Spróbuj raz jeszcze.")


print("Podane liczby to:", result)
