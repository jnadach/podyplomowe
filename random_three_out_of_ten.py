import random

# random_numbers = []
#
# while len(random_numbers) < 3:
#     num = random.randint(1, 10)
#     if num not in random_numbers:
#         random_numbers.append(num)
#
# random_numbers.sort()
# print(random_numbers)

numbers = [i for i in range(1, 11)]
random_numbers = random.sample(numbers, 3)
random_numbers.sort()
print(random_numbers)




