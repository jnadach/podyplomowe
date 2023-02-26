# 1 1 2 3 5 8 13 21 34 ...

def fib_rec(n):
    if n < 1:
        return None
    elif n < 3:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

#print(fib_rec(8))

def fib(n):
    if n < 1:
        return None
    elif n < 3:
        return 1
    el1 = el2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = el1 + el2
        el1, el2 = el2, sum
    return sum

for n in range(1, 101):
    print(n, "->", fib_rec(n))