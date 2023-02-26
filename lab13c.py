# Jan Nadachowski

import random

letters = ["A", "B", "C", "D", "E"]


def fruit_machine(letters):
    result = ["A", "B", "C"]
    counter = 0
    while (result[0] != result[1]) or (result[1] != result[2]):
        for i in range(0, len(result)):
            result[i] = random.choice(letters)
        counter += 1
        print("Proba numer", counter, result)


fruit_machine(letters)
