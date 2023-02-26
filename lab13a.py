#Autor: Jan Nadachowski

def power(numbers, p):
    """
    :param numbers: lista liczb
    :param p: potęga
    :return: lista liczb podniesionych do potęgi p
    """
    return [num ** p for num in numbers]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = power(numbers, 2.4)
print(result)
