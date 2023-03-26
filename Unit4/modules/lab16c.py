# Autor: Jan Nadachowski
# Zmodyfikuj moduł lotto, aby dawał możliwość grania systemem tj. pozwalał
# skreślać od 6 do 12 liczb.

from random import sample


def draw_numbers():
    numbers = [i for i in range(1, 50)]
    lucky_numbers = sample(numbers, 6)
    lucky_numbers.sort()
    return lucky_numbers


def get_game_system():
    while True:
        try:
            n = int(input("Podaj ile liczb chcesz wybrać (z przedziału 6 - 12): "))
            if n < 6 or n > 12:
                print("Należy podać liczbę z przedziału 6  - 12.")
                continue
            break
        except:
            print("To nie jest liczba.")
            continue
    return n


def get_user_numbers():
    n = get_game_system()
    counter = 1
    user_numbers = []
    while counter < n + 1:
        try:
            number = int(input("Podaj " + str(counter) + " liczbę (1 - 49): "))
            if number in user_numbers:
                print("Powtórzona liczba!")
                continue
            if number < 1 or number > 49:
                print("Należy podać liczbę z przedziałi 1 - 49!")
                continue
        except:
            print("To nie jest liczba!")
            continue

        user_numbers.append(number)
        counter += 1
    user_numbers.sort()
    return user_numbers


def check_numbers(user_numbers, lucky_numbers):
    counter = 0
    for i in user_numbers:
        if i in lucky_numbers:
            counter += 1
    return counter


if __name__ == "__main__":
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_numbers(user_numbers, lucky_numbers)
    print(user_numbers)
    print(lucky_numbers)
    print(result)

