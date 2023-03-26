# Author: Jan Nadachowski
# Dokonaj odpowiednich zmian w programie do rzucania kośćmi do gry (dices.py), aby
# zabezpieczyć zmienne instancji przed przypadkowym nadpisaniem (enkapsulacja).

import random


class Dice:

    def __init__(self):
        self.__value = None

    def throw(self):
        self.__value = random.randint(1, 6)

    def __str__(self):
        return "[{}]".format(self.__value)


class DicePair:

    def __init__(self):
        self.__pair = [Dice(), Dice()]

    def throw(self):
        self.__pair[0].throw()
        self.__pair[1].throw()

    def is_double(self):
        return self.__pair[0]._Dice__value == self.__pair[1]._Dice__value

    def __str__(self):
        return str(self.__pair[0]) + str(self.__pair[1])


dices = DicePair()
while True:
    dices.throw()
    print(dices)
    if dices.is_double():
        break
