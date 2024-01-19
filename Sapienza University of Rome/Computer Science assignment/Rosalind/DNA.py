f = open('Rosalind/rosalind_dna.txt').read()
dic = {'A':0, 'C':0, 'G':0, 'T':0}
for a in f:
    if a == 'A':
        dic['A'] += 1
    elif a == 'T':
        dic['T'] += 1
    elif a == 'C':
        dic['C'] += 1
    elif a == 'G':
        dic['G'] += 1

print( dic)

