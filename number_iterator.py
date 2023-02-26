import random


def generate_numbers(total_numbers):
    numbers = []
    for i in range(total_numbers):
        numbers.append(random.randint(1, 99))
    return numbers

print(generate_numbers(10))
print(generate_numbers(20))
print(generate_numbers(30))
print(generate_numbers(40))