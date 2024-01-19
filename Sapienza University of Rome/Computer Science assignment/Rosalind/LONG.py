from Bio import SeqIO
f = SeqIO.parse('D:\Cartelle Utente\Download/rosalind_long.txt', 'fasta')
dict = {}
for a in f:
    dict[a.id] = a.seq  # dict to access to the seq from the id 
import networkx as nx


G = nx.DiGraph()                                                       # unique way to unify the sequences
for seq_id in dict:                                                 # overlap more than half of the sequence
    n = len(dict[seq_id])//2
    for seq_id2 in dict:
        if dict[seq_id][:n] in dict[seq_id2] and dict[seq_id] != dict[seq_id2]:  # create a graph wiht 
            m = 0
            G.add_edge(seq_id2,seq_id)
                

di = {}
for a in dict:      # dictionary to collect data about nodes and to find the first seq
    di[a] = [0 , 0]
for a in G.edges():
    di[a[0]][0] += 1  # egdes starting from the node
    di[a[1]][1] += 1  # edges ending on the node


def connectstring(a, b):  # a string on the left. b string on th right
    sub = a[-100:]  # substing
    n = 0
    m = 100
    pos = 0
    while n < (len(b)-m+1):
        r_frame = b[n:n+m]   # I set the reading frame equal to len of substring
        if r_frame == sub:     #when i found a substring i immediatly save position in the list
            pos = n+m
            break
        n += 1
    return int(pos)

for a in di:
    if di[a][1] == 0:   # startin seq = node having no edges ending on it
        node = a  
s = dict[node] #string where ill save the complete seq
for a in di:    
    for b in nx.neighbors(G,node):   # loop to axcess neighbor node of each node
        next_node = b
    if next_node == node:
        break
    cut_position = connectstring(dict[node], dict[next_node])  # function to find the point of join of two neighbors string
    s = s + dict[next_node][cut_position:]
    node = next_node

print(s)