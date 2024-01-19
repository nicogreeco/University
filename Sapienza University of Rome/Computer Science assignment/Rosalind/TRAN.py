from Bio import SeqIO
f = SeqIO.parse('C:/Users/nicco/Downloads/rosalind_tran.txt', 'fasta')
list = []
for record in f:
    list.append(record.seq)

n = 0
dict = {'transition': 0 , 'transvertion': 0}
purin = ('A','G')
pyrimidine = ('T', 'C')

while n < len(list[0]):
    if list[0][n] != list[1][n]:
        if list[0][n] in purin and list[1][n] in purin:
            dict['transition'] += 1
        elif list[0][n] in pyrimidine and list[1][n] in pyrimidine:
            dict['transition'] += 1
        else:
            dict['transvertion'] += 1   
    n += 1

print(dict['transition']/dict['transvertion'])