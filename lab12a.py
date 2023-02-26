#Autor: Jan Nadachowski

def get_and_print(iteration=10, horizontal_print=True):
    char = input("Podaj dowolny znak: ")
    if horizontal_print:
        print(char*iteration)
    else:
        for i in range(iteration):
            print(char)

#Horizontal
get_and_print()

#Vertical
get_and_print(horizontal_print=False)
