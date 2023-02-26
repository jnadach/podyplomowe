#Autor: Jan Nadachowski

# mniej niż 16 - wygłodzenie
# 16 - 16.99 - wychudzenie
# 17 - 18.49 - niedowaga
# 18.5 - 24.99 - wartość prawidłowa
# 25 - 29.99 - nadwaga
# 30 - 34.99 - I stopień otyłości
# 35 - 39.99 - II stopień otyłości
# powyżej 40 - otyłość skrajna


def get_BMI(hight, weight):
    return weight / ((hight/100)**2)


def get_category(BMI):
    if BMI < 18.5:
        return "niedowagę"
    elif BMI < 25:
        return "wagę prawidłową"
    elif BMI < 30:
        return "nadwagę"
    else:
        return "otyłość"


hight = int(input("Podaj wzrost w cm: "))
weight = int(input("Podaj wagę w kg: "))

print("Twój wskaźnik BMI wynosi: ", get_BMI(hight, weight))
print("Masz", get_category(get_BMI(hight, weight)))
