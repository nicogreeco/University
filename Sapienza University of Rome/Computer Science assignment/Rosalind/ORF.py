from Bio import SeqIO
from Bio.Seq import Seq

with open('Rosalind/rosalind_orf.txt') as rosalind:
    my_seq = SeqIO.read(rosalind, "fasta").seq   # read the seq
    sol = []
    n = 0
    while n < len(my_seq):
        if my_seq[n:n+3] == 'ATG':   # scanning the seq lookin for start codon
                    seq_for_trans = my_seq[n:] # seq down the ATG codon
                    if seq_for_trans[-3:]  in ['TAG','TGA','TAA'] or seq_for_trans.translate(to_stop = True) != seq_for_trans.translate():
                        sol.append(seq_for_trans.translate(to_stop = True))    # check that the translated string ended because of a 
        n += 1                                                                 # stop codon instead of th end of the DNA string

    my_seq = my_seq.reverse_complement()  
    n = 0
    
    while n < len(my_seq):              # do the same thing with the reverse of the DNA string
        if my_seq[n:n+3] == 'ATG':
                    seq_for_trans = my_seq[n:]
                    if seq_for_trans[-3:]  in ['TAG','TGA','TAA'] or seq_for_trans.translate(to_stop = True) != seq_for_trans.translate():
                        sol.append(seq_for_trans.translate(to_stop = True))


        n += 1
    sol = list(dict.fromkeys(sol)) # eliminate from the list any duplicates
    for a in sol:
        print(a)