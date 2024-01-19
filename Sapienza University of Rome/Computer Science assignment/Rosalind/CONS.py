f = open('Rosalind/rosalind_cons.txt').read()
dnaseq = list(f.split('>'))
n = 0
dnaseq.remove('')

while n < len(dnaseq):
    dnaseq[n] = dnaseq[n].replace('\n', '')   # open the file and move dna sequences
    dnaseq[n] = dnaseq[n][13:]                # into a list
    n += 1
    

dic = {'A':[0 for a in range(len(dnaseq[0]))],
    'C':[0 for a in range(len(dnaseq[0]))],     # crated a dictionary where will save number of 
    'G':[0 for a in range(len(dnaseq[0]))],     # each nucleotide for each position n of the strings
    'T':[0 for a in range(len(dnaseq[0]))]}
cons = []  # list to save the cons seq
n = 0
while n < len(dnaseq[0]):
    for a in dnaseq:
        if a[n] == 'A':
            dic['A'][n] += 1
        elif a[n] == 'T':           # addition to the dictionary according
            dic['T'][n] += 1        # to the nucleotide at n position of each string
        elif a[n] == 'C':   
            dic['C'][n] += 1
        elif a[n] == 'G':
            dic['G'][n] += 1
    maxx = 0
    for a in dic:
        if dic[a][n] > maxx:   # find the higest value of nucleotides and
            maxx =dic[a][n]    # add it to the list containing the consensous sequence
            nucleotide = a
    cons.append(nucleotide)
    n += 1
    maxx = 0

cons = ''.join(cons)
print(cons)                  # printing of the cons seq
#print('A:', *dic['A'])       # printing of matrix
#print('C:', *dic['C'])
#print('G:', *dic['G'])
#print('T:', *dic['T'])



    
