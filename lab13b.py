#Autor: Jan Nadachowski

def tab_monzenia(n, m):
    if n < 1:
        return
    for i in range(1, m+1):
        print(f"{n} x {i} = {i * n}")
    tab_monzenia(n-1, m)

tab_monzenia(10, 10)


