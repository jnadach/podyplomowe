# Autor: Jan Nadachowski
# • zaimportuj utworzony moduł i skorzystaj z jego funkcji.
from lab_16b_modul import verify_ints_in_list, sum_list_elem, product_list_elem

lst = [1, 2, 3, "aa", 5]
print("Nasza lista to:", str(lst))
if verify_ints_in_list(lst):
    print("Suma elementow listy: ", sum_list_elem(lst))
    print("Iloczyn element ow listy: ", product_list_elem(lst))
else:
    print("Lista nie jest listą liczb całkowitych")
