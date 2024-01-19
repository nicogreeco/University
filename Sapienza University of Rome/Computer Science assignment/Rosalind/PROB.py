import math
f = open('Rosalind/rosalind_prob.txt').read()
l = list(f.split())
s = l.pop(0)
sol = []
for a in l:
    CG = float(a)
    C = G = CG/2
    A = T = (1-CG)/2
    P = 1
    for a in s:
        if a == 'A':
            P = P*A
        elif a == 'T':
            P = P*T
        elif a == 'C':
            P = P*C
        elif a == 'G':
            P = P*G

    sol.append(math.log(P,10))
print(*sol)