class MyClass:
    x = 5

    def __init__(self):
        self.y = 9

obj = MyClass()

print(obj.x, obj.y)

print(MyClass.__dict__)
print(obj.__dict__)
print()
setattr(obj, "z", 1) #refleksja
print(getattr(obj, "x")) # introspekcja

print("z:", obj.z)





# class A:
#     pass
#
# class B:
#     pass
#
# class C(A, B):
#     pass
#
# print(C.__bases__)
#
# for c in C.__bases__





# class MyClass:
#
#     def __init__(self, name):
#         self.__name = name
#
#     def __my_private_method(self):
#         print("To jest metoda prywatna")
#
#     def my_public_method(self):
#         self.__my_private_method()
#         print("To jest metoda publiczna")
#
#
# obj = MyClass("Jan")
# obj.my_public_method()
#
# print(obj.__dict__)
# print(MyClass.__dict__)
#
# print()
# print(MyClass.__name__)
# print(type(obj).__name__)
# print(type(obj).__module__)




# class MyClass:
#
#     def __init__(self, name):
#         self.__name = name
#         print("Inicjalizuję obiekt!")
#
#     def get_name(self):
#         return self.__name
#
# obj = MyClass("Jan")
# print("Mam na imię", obj.get_name())




# class MyClass:
#     y = 99
#
#     def my_method(self, x):
#         self.other_method()
#         print("To jest moja metoda z paramterem:", x, "i zmienną klasy", MyClass.y)
#
#     def other_method(self):
#         print("To jest metoda", self.y)
#
# obj = MyClass()
# obj.my_method(123)





# class MyClass:
#
#     def __init__(self, x=1):
#         if x % 2 == 0:
#             self.a = x
#         else:
#             self.b = x
# obj = MyClass(22)
#
# if hasattr(obj, "a"):
#     print(obj.a)
# else:
#     print(obj.b)










# class MyClass:
#
#     __counter = 0 #Zienna klasy wspólna dla clałej klasy obiektów
#
#     def __init__(self, x=1):
#         self.__x = x
#         MyClass.__counter += 1
#
# obj1 = MyClass(1)
# obj2 = MyClass(2)
# obj3 = MyClass(77)
#
# print(obj1.__dict__, obj1._MyClass__counter)
# print(obj2.__dict__, obj2._MyClass__counter)
# print(obj3.__dict__, obj3._MyClass__counter)
#
# print("Ile obiektów?:", MyClass._MyClass__counter)
#
# print(MyClass.__dict__)


















# class MyClass:
#     def __init__(self, x=1):
#         self.__x = x
#
#     def sety(self, y):
#         self.__y = y
#
# obj1 = MyClass()
#
# obj2 = MyClass(4)
# obj2.sety(7)
#
# obj3 = MyClass(3)
# obj3.z = 99
#
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
#
# print(obj1._MyClass__x)
