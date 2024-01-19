f = open('Rosalind/Codons.txt').read()
l = f.replace('      ', ',').replace('   ', ',').replace('\n', ',')
l = list(l.split(','))
dic = {}
for a in l:               # from the genetic code I found on Rosalind, which I saved on a txt
    dic[a[:3]] = a[4:]    # I create a dictionary having codons as keys storing for the letter
                          # of the amminnnoacid
f = open('Rosalind/rosalind_prot.txt').read()
n = 0
sol = []
while n < (len(f)-3):
    r_frame = f[n:n+3]
    if dic[r_frame] != 'Stop':
        sol.append(dic[r_frame])
    else:
        break
    n += 3
print(''.join(sol))
