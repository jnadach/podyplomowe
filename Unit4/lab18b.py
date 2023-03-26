# Autor: Jan Nadachowski
# Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
# liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b':
# 2, 'r': 2, 'c': 1, 'd': 1 }.

def count_duplicates(input):
    result = {}
    for c in input:
        if c not in result.keys():
            result[c] = input.count(c)
    return result


print(count_duplicates("abracadabra"))
