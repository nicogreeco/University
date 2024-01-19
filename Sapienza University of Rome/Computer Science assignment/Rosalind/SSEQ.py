from Bio import SeqIO
f = SeqIO.parse('C:/Users/nicco/Downloads/rosalind_sseq.txt', 'fasta')

list = []
for record in f:
    list.append(record.seq)

subseq = list[1]
seq = list[0]
solution =  []
n = 0

for nuc in subseq:
    while n < len(seq):
        if nuc == seq[n]:
            solution.append(str(n+1))
            n += 1
            break
        else:
            n += 1
if len(solution) != len(subseq):
    print('there are some prob')

print(*solution)