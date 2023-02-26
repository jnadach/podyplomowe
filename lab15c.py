# Zabezpiecz program zliczający punkty w grach (moduł 14, lab 3) przed
# wprowadzaniem błędnych danych przez użytkownika.

# Autor: Jan Nadachowski


def get_players():
    results = {}
    while True:
        try:
            number_of_players = int(input("Podaj liczbę graczy: "))
            break
        except:
            print("Podano błędną wartość, spróbuj raz jeszcze.")

    counter = 0
    while counter < number_of_players:
        try:
            name = input("Podaj gracza: ")
            assert isinstance(name, 'str')
            results[name] = 0
            counter += 1
        except:
            print("Podano nieprawidłowe imię gracza, spróbuj raz jeszcze.")
    return results


def get_treshold():
    while True:
        try:
            points_threshold = int(input("Podaj liczbę punktów potrzebnych do wygranej: "))
            break
        except:
            print("Podano błędną wartość, spróbuj raz jeszcze.")
    return points_threshold


def check_winner(results, points_threshold):
    for player in results:
        if results[player] >= points_threshold:
            return player
    return False


def check_if_draw(results):
    winners_list = []
    for player in results:
        if results[player] >= points_threshold:
            winners_list.append(player)
    return winners_list


def update_socres(name, points, results):
    results[name] = points


def play_game(results, points_threshold):
    counter = 1
    while not check_winner(results, points_threshold):
        print("Tura", counter)
        for player in results:
            while True:
                try:
                    score = int(input(f"Podaj punktację dla gracza {player}: "))
                    update_socres(player, score, results)
                    break
                except:
                    print("Podano błędną wartość, spróbuj raz jeszcze.")
        counter += 1
    print("--------------------------------------------------------------------")
    print("Ostateczna punktacja: ", results)


def display_results(winner, results):
    if len(check_if_draw(results)) > 1:
        print("Remis! Wygrywają:", check_if_draw(results))
    else:
        print("Gratulacje, wygrywa:", winner, "z liczbą punktów:", results[winner])


# ------------------------------------------------------------------------------------

results = get_players()
points_threshold = get_treshold()
play_game(results, points_threshold)
winner = check_winner(results, points_threshold)
display_results(winner, results)
