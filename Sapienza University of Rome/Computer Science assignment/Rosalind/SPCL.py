from Bio import SeqIO
from Bio.Seq import Seq

with open('C:/Users/nicco/Downloads/rosalind_splc.txt') as rosalind:
    seq = list(SeqIO.parse(rosalind, "fasta"))
    gene = seq.pop(0).seq # the first record is the main DNA seq of the gene

for intron in seq:
    n = 0
    while n < (len(gene)-len(intron.seq)):     # look for the introns seq in the gene
        if gene[n:n+len(intron.seq)] == intron.seq:  
            gene = F"{gene[:n]}{gene[n+len(intron.seq):]}"  # when find the introns i remove it from the gene
        n += 1
gene = Seq(gene)
p = gene.translate(to_stop = True) # translate

print(p)