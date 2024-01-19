lista = []
for n in range(int(input())):
    name = input()
    score = float(input())
    lista.append([score,name])
lista.sort()
sol = []
counter=1
while counter <= len(lista):
    if lista[counter][0] == lista[0][0]:
        del lista[counter]
    else:
        break

for student in lista:
    if student[0] == lista[1][0]:
        sol.append(student[1])
for element in sol:
    print(element)