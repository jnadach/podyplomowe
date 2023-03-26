class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class StackSum(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val



obj = StackSum()
obj2 = StackSum()



obj.push(3)
obj.push(2)
obj.push(1)

obj2.push(4)
obj2.push(4)
obj2.push(4)

print("stos 1:", obj.get_sum())
print("stos 2:", obj2.get_sum())

print(obj.pop())
print(obj.pop())
print(obj.pop())

print(obj2.pop())
print(obj2.pop())
print(obj2.pop())

print("stos 1:", obj.get_sum())
print("stos 2:", obj2.get_sum())

