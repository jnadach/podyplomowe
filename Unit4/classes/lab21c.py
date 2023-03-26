# Author: Jan Nadachowski
# Rozbuduj klasę Stack o następujące metody:
# • empty() - powinna zwracać True jeżeli stos jest pusty, w przeciwnym wypadku zwracać False,
# • size() - powinna zwracać rozmiar stosu,
# • top() - powinna zwracać "górny" element stosu, czyli ten, który zostanie "ściągnięty"
# metodą pop().

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def empty(self):
        return len(self.__stack_list) == 0

    def size(self):
        return len(self.__stack_list)

    def top(self):
        if self.size() == 0:
            return None
        else:
            return self.__stack_list[-1]


print("Tworze stost.")
stack1 = Stack()
print("Stos jest pusty?:", stack1.empty())
print("Rozmiar stosu?:", stack1.size())
print("Ostatni element sotsu?:", stack1.top())
print()
print("Dodaje elementy stosu: 100, 200, i 300.")
stack1.push(100)
stack1.push(200)
stack1.push(300)
print("Usuwam ostani element stosu:", stack1.pop())
print()
print("Stos jest pusty?:", stack1.empty())
print("Rozmiar stosu?:", stack1.size())
print("Ostatni element sotsu?:", stack1.top())
