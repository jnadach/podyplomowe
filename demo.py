# numbers = [1, 2, 3]
# print(numbers)
#
# numbers[0], numbers[1] = numbers[1], numbers[0]
# print(numbers)

# numbers = [i ** 2 for i in range(101)]
# numbers = [i ** 2 for i in range(101) if i % 2 == 0]
# print(numbers)


# numbers = [i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]
# print(numbers)
# print(len(numbers))

# def scope_test():
#     global x
#     x += 1
#
#
# x = 99
# print(x)
# scope_test()
# print(x)
#
#
# def change_value(n):
#     print("przed zmianą:", n)
#     n = [3, 4]
#     print("po zmianie:", n)
#
#
# val = [1, 2]
# change_value(val)
# print(val)


# def recursion(number):
#     if number == 20:
#         return
#     print(number)
#     number += 1
#     recursion(number)
#
# recursion(1)

# Krotka
def my_fubc(*args):
    for el in args:
        print(el)


# my_fubc(1,2,3,4,5)

# Slownik
def my_fubc(**args):
    for el in args.items():
        print(el)


# my_fubc(val1="raz", cal2=999)

# Krotki
# numbers = (1, 2, 3)
# numbers2 = 1, 2, 3
# numbers3 = ()
# numbers4 = 1,
# numbers5 = tuple(x for x in range(10))
#
# print(numbers5)
#
# a = 1, 2
# x, y, z = numbers
# print(x)
# print(y)
# print(z)
#
#
# nums = [1,2,3]
# t_nums = tuple(nums)
# print(t_nums)
# l_nums = list(t_nums)
# print(l_nums)

# phones = {
#     "Tomek": 342354650,
#     "Ada": 345234321,
#     "Karol": 965876590,
#     "Tomek": 1000000000000
# }
# print(phones)

# animals_dict = {
#     "kot": "cat",
#     "pies": "dog",
#     "chomik": "hamster"
# }
#
# print(animals_dict["kot"])
# print(animals_dict.get("kot"))
# print(animals_dict.get("krowa"))
# print(animals_dict.get("krowa", "Nie ma klucza"))
# #print(animals_dict["krowa"])
#
# words = ["kot", "lew", "chomik"]
# # for word in words:
# #     if word in animals_dict:
# #         print(word, "->", animals_dict[word])
# #     else:
# #         print("Nie znleziono slowa", word, "w słowniku.")
#
# #To jest tozsame:
# for key in animals_dict.keys():
#     print(key, "->", animals_dict[key])
#
# #do tego
# for key in animals_dict:
#     print(key, "->", animals_dict[key])
#
# for i in animals_dict.items():
#     print(i)
#
# for pl, en in animals_dict.items():
#     print(pl, "->", en)
#
#
# animals_dict["świnka"] = "pig"
# animals_dict.update({"lis": "fox"})
# animals_dict.update({"świnka": "piggy"})
#
# animals_dict2 = animals_dict.copy()
#
# del animals_dict2["świnka"]
# animals_dict2.popitem()
#
# print(animals_dict2)
#
# animals_dict2.clear()
# print(animals_dict2)

try:
    print(1/0)
except:
    print("Ups!")