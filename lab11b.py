#autor: Jan Nadachowski

user_input = []
counter = 0

while counter < 1:
    user_num = input("Podaj liczbę (w celu zakonczenia naciśnij enter): ")
    if user_num == "":
        counter += 1
    else:
        user_input.append(int(user_num))

user_input_dedupe = []

for i in user_input:
    if i not in user_input_dedupe:
        user_input_dedupe.append(i)

user_input_dedupe.sort(reverse=True)

print(user_input_dedupe)
