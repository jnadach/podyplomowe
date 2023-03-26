# char1 = "a"
# char2 = " "
#
# print(ord(char1))
# print(ord(char2))
#
# print()
#
# print(ord("ę"))
# print(hex(ord("ę")))
#
# print("\u0119")

# c = "a"
# print(c, ord(c), hex(ord(c)), c.encode())
#
#
# print()
#
# c = "\u20AC"
# print(c, ord(c), hex(ord(c)), c.encode())

# print(chr(97))
# print(chr(945))
#
# print("a" == chr(ord("a")))



alfabet = ""
for i in range(ord("A"), ord("Z")+1):
    alfabet += chr(i)

print(alfabet)

print(ord("ą"))
print(ord("ę"))
print(ord("ł"))
print(ord("ń"))
print(ord("ó"))
print(ord("ś"))
print(ord("ź"))
print(ord("ż"))


