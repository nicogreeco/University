S = 'UAGAGCGCAACAUCAUUCUGUGGGUAACGCCCAUGUUACUUAGCAUGGCAAGCCCCGUAGCUAUCAGGGUCAUG'
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()


n = 0
while n < len(S):
    l = S[n] + str(n)
    G.add_node(l)
    n += 1
a = list(G.nodes())
n = 0
while n < len(a)-1:
    G.add_edge(a[n], a[n+1])
    n += 1
basepair = [
    ('A', 'U'),
    ('U', 'A'),
    ('G', 'C'),
    ('C', 'G'),
    
]
for a in G.nodes():
    for b in G.nodes():
        if (a[0],b[0]) in basepair:
            G.add_edge(a,b)


nx.draw_circular(G, with_labels=True, font_weight='bold')

def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

print(factorial(S.count("A"))*factorial(S.count("G")))






