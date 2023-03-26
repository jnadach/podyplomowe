# Autor: Jan Nadachowski
# Korzystając z odpowiednich modułów napisz skrypt realizujący następujące zadania:

import platform
import random
import math

# • wyświetl informacje o procesorze komputera,
print("Twój komputer posiada processor:", platform.processor())


# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
lst = [i for i in range(1, 11)]
result = random.sample(lst, 3)
result.sort()
print("Wylosowane liczby to:", result)


# • wyznacz sinus 90 stopni.
print("Sinus kąta 90 stopni wynosi:", str(math.sin(math.radians(90))))