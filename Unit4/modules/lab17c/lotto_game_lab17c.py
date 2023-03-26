import sys

sys.path.append("\\\\fs1\\FolderRedir-Student\\nadachow\\Desktop\\packages")

from games.lotto import get_user_numbers, draw_numbers, check_numbers

print("Witaj w grze lotto!")
user_numbers = get_user_numbers()
print("Podane liczby to: ", user_numbers)

print("\nNaciśnij ENTER, aby dokonać losowania liczb!\n")
input()
lucky_numbers = draw_numbers()
print("Wylosowane licby to:", lucky_numbers)

result = check_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("GRATULACJE!!!", "Jesteś milionerem!")
elif result == 5:
    print("BRAWO!", "Trafiono piątkę.", "Zgarniesz sporą sumkę.")
elif result == 4:
    print("HURRA!", "Trafiono czwórkę.", "To całkiem niezły wynik.")
elif result == 3:
    print("Trafiono trójkę.", "Przysługuje Ci minimalna wygrana.")
elif result == 2 or result == 1:
    print("Trafiono", str(result), "liczbę. Było bardzo blisko.")
else:
    print("To nie jest Twój dzień!")
