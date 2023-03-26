# Jan Nadachowski
# Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
# wraz z punktami kodowymi dla każdej litery.


def get_alphabet():
    alfabet = ""
    for i in range(ord("a"), ord("z") + 1):
        alfabet += chr(i)
    return alfabet


def add_polish_letters(alphabet):
    polish_alphabet = alphabet[:]
    polish_letters = ["ą", "ę", "ł", "ń", "ó", "ś", "ź", "ż"]
    for letter in polish_letters:
        polish_alphabet += letter
    return polish_alphabet


def print_alphabet(alphabet):
    for letter in alphabet:
        print(letter, "-->", str(ord(letter)))


print_alphabet(add_polish_letters(get_alphabet()))
