# Autor: Jan Nadachowski

def get_perimeter(a, b):
    return (2 * a) + (2 * b)


def get_area(a, b):
    return a * b


def get_diagonal(a, b):
    return (a ** 2 + b ** 2) ** 0.5


def rectangle_param(a, b):
    print("Prostokąt o bokach", a, "i", b, "posiada następujące wymiary:")
    print("Obwód: ", get_perimeter(a, b))
    print("Pole pow.: ", get_area(a, b))
    print("Przekątna: ", get_diagonal(a, b))


print("____________________________________")
rectangle_param(4, 5)
print("____________________________________")
rectangle_param(2678, 5678)
print("____________________________________")
rectangle_param(344555, 788998)
