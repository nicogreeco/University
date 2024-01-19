import matplotlib.pyplot as plt
import networkx as nx
G = nx.DiGraph()
l = list(map(int, '5 1 4 2 3'.split()))
G.add_nodes_from(l)

for a in l:
    for b in l:
        if a > b and l.index(a) < l.index(b):
            
            G.add_edge(a, b)
nx.dag_longest_path(G)

G = nx.DiGraph()
G.add_nodes_from(l)

for a in l:
    for b in l:
        if a < b and l.index(a) < l.index(b):
            
            G.add_edge(a, b)
nx.dag_longest_path(G)