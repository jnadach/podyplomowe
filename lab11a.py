#autor: Jan Nadachowski

import random

user_input = []
counter = 1
comp_input = random.sample(range(50), 6)

while counter < 7:
    user_num = int(input("Podaj liczbę " + str(counter) + " z zakresu od 0 do 49: "))
    if user_num > 49 or user_num < 0:
        print("Podano liczbę spoza zakresu")
    elif user_num not in user_input:
        user_input.append(user_num)
        counter += 1
    elif user_num in user_input:
        print("Podano tą samą liczbą ponownie. Spróbuj jeszcze raz")

guess_num = 0

for i in user_input:
    if i in comp_input:
        guess_num += 1

user_input.sort()
comp_input.sort()

print("Wybrane liczby:",user_input)
print("Liczby wylosowane przez komputer:", comp_input)
print("Liczba trafień:", guess_num)
