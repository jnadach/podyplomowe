letters = ["a", "f", "z", " ", "b", "A"]

# numbers = [4, 5, 2, 10, 100, 1, 2, 2, 230, -2, -444]
#
# swapped = True
#
# while swapped:
#     swapped = False
#     for i in range(len(numbers) - 1):
#         if numbers[i] > numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#             swapped = True

print(letters)
letters.sort()
print(letters)

print([ord(l) for l in letters])

