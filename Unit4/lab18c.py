# Autor: Jan Nadachowski
# Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem
# cezara z parametrem przesunięcia równym 3.
#
# VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ

def get_alphabet():
    alfabet = ""
    for i in range(ord("A"), ord("Z") + 1):
        alfabet += chr(i)
    return alfabet


def decode_cesar_code(code, alphabet, move):
    decoded = ""
    head = alphabet[:move]
    tail = alphabet[(-1 * move):]
    for char in code:
        if char in head:
            decoded += tail[head.index(char)]
        elif char in alphabet:
            decoded += chr(ord(char) - move)
        else:
            decoded += char
    return decoded


def code_cesar_code(code, alphabet, move):
    coded = ""
    head = alphabet[:move]
    tail = alphabet[(-1 * move):]
    for char in code:
        if char in tail:
            coded += head[tail.index(char)]
        elif char in alphabet:
            coded += chr(ord(char) + move)
        else:
            coded += char
    return coded


code = "VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ"
alphabet = get_alphabet()

print("Wiadomość zaszyfrowana:", code)
print("Wiadomość odszyfrowana:", decode_cesar_code(code, alphabet, 3))
print()

code = "STUDIA PODYPLOMOWE - PROGRAMISTA PYTHON"
print("Wiadomość zaszyfrowana:", code)
print("Wiadomość odszyfrowana:", code_cesar_code(code, alphabet, 3))
print()

code = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
print("Wiadomość zaszyfrowana:", code)
print("Wiadomość odszyfrowana:", code_cesar_code(code, alphabet, 5))
print()

code = "YMJ VZNHP GWTBS KTC OZRUX TAJW YMJ QFED ITL"
print("Wiadomość zaszyfrowana:", code)
print("Wiadomość odszyfrowana:", decode_cesar_code(code, alphabet, 5))
print()