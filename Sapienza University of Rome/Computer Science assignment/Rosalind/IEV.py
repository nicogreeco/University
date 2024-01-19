f = open('Rosalind/rosalind_iev.txt').read()
l = list(map(int,f.split()))

# 0 = AA-AA, 1 = AA-Aa, 2 = AA-aa, 3 = Aa-Aa, 4 = Aa-aa, 5 = aa-aa
E = (l[0]+l[1]+l[2])*2 + l[3]*2*0.75 + l[4]*2*0.5
print(E)