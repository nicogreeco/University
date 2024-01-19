f = open('Rosalind/Codons.txt').read()
l = f.replace('      ', '-').replace('   ', '-').replace('\n', '-')
l = list(l.split('-'))
dic = {}
for a in l:
    amm = a[4:]
    if amm not in dic:
        dic[amm] = 1         # starting from genetic  code ill create a dictionary
    else:                    # that has amm as keys and the number of codon that
        dic[amm] += 1        # encode them as value
f = open('Rosalind/rosalind_mrna.txt').read()
P = 1
for nucl in f:
    P = P*dic[nucl]
P = P*dic['Stop']          # calculating all possible combination
print(P%1000000) 