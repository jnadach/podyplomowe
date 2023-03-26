# Autor: Jan Nadachowski
# 2. Korzystając z napisanej wcześniej klasy Stack:

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


# • utwórz 3 stosy (3 obiekty klasy Stack),
stack1 = Stack()
stack2 = Stack()
stack3 = Stack()

# • połóż na pierwszym stosie kolejno liczby od 1 do 100,
for i in range(1, 101):
    stack1.push(i)

# • ściągaj kolejne elementy (liczby) z pierwszego stosu i umieszczaj na drugim,
for i in range(1, 101):
    stack2.push(stack1.pop())

# • ściągaj kolejne elementy z drugiego stosu i umieszczaj na trzecim,
for i in range(1, 101):
    stack3.push(stack2.pop())

# • ściągaj i wyświetlaj w tej samej linii elementy z trzeciego stosu.
for i in range(1, 101):
    print(stack3.pop(), end=",")
