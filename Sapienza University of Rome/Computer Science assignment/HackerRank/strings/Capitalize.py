def solve(s):
    lista = list(s)
    if lista[0].isupper() == False:
        lista[0] = lista[0].upper()
    for a in range(len(lista)):
        if lista[a]==' ':
            lista[(a+1)] = lista[(a+1)].upper()
    sol = ""
    return sol.join(lista)
s = input()
print(solve(s))