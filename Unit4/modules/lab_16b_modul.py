# Autor: Jan Nadachowski
# Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
# • stwórz modułu o dowolnej nazwie,

# • dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
def verify_ints_in_list(list):
    for i in list:
        if not isinstance(i, int):
            return False
    return True


# • dodaj funkcję sumującą wszystkie liczby z listy,
def sum_list_elem(list):
    sum = 0
    for i in list:
        sum += i
    return sum


# • dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
def product_list_elem(list):
    product = 1
    for i in list:
        product *= i
    return product


# • dodaj testy weryfikujące poprawne działanie napisanych funkcji,
if __name__ == "__main__":
    error_list = [1, "aa", 2]
    valid_list = [1, 2, 3, 4]

    print("Test funkcji verify_ints_in_list():")
    print(verify_ints_in_list(error_list) is False)
    print(verify_ints_in_list(valid_list) is True)

    print("Test funkcji sum_list_elem():")
    print(sum_list_elem(valid_list) == 10)
    print(sum_list_elem(valid_list) != 100)

    print("Test product_list_elem():")
    print(product_list_elem(valid_list) == 24)
    print(product_list_elem(valid_list) != 240)


