f = open('Rosalind/monoisotopic_mass_table.txt')
dic = {}
for line in f:
    dic[line[0]] = float(line[4:])

total_mass = 0
f = open('Rosalind/rosalind_prtm.txt').read()
for amm in f:
    total_mass += dic[amm]
print(total_mass)
