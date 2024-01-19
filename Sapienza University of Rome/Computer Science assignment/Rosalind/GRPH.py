import networkx as nx
from Bio import SeqIO

records = list(SeqIO.parse('Rosalind/rosalind_gc.txt', "fasta"))
# open the txt file in fasta format with SeqIO

G = nx.DiGraph()  # directed graph with network x
for a in records:
    G.add_node(a.id)  # .id acces directly to id of the SeqIO object frmo the fasta format
for a in records:
    for b in records: # .seq access to the DNA string of the object 
        if a.id != b.id and a.seq[-3:] == b.seq[:3]: # compare last codon of a with first of b
                G.add_edge(a.id, b.id)   # add directed edge if are equal

for a in G.edges:
    print(' '.join([i for i in a])) # print all edges