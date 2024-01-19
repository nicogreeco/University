inpu = input().split()
n, m = int(inpu.pop(0)), int(inpu.pop(0))

trattini = '---'
pisbello = '.|.'
lista=[]
for a in range(int((n-1)/2)):
    linea = ''
    decorazione = '.|.'
    x = int((n-1)/2) - a
    for b in range(x):
        linea = F"{linea}{trattini}"
    if a != 0:
        for c in range(a):
            decorazione = F"{decorazione}{pisbello}{pisbello}"
    line= F"{linea}{decorazione}{linea}"
    lista.append(line)

welcome = '-WELCOME-'
for a in range(int((m-9)/6)):
    welcome = F"{trattini}{welcome}{trattini}"
lista.append(welcome)

for a in reversed(range(int((n-1)/2))):
    lista.append(lista[a])
for a in lista:

    print(a)
