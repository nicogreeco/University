import networkx as nx
f = open('C:/Users/nicco/Downloads/rosalind_tree.txt').read() # open the file and divide the number of nodes n from the edges
l = f.split('\n') # set of edges
n = int(l.pop(0)) # number of nodes

G = nx.Graph()
for i in range(1,n+1):
    G.add_node(i) # adding nodes to graph

for i in l:
    edge = list(map(int,i.split()))
    G.add_edge(edge[0],edge[1])   # adding edges to the graph

print(nx.number_connected_components(G)-1) 
# the minimun number of edges needed to add to the graph are equal to the number of connecetd sub-graph minus one.
# to create a tree we just need to create a fully connected graph (having said from the instruction that the input has no cycle),
# so making one edge between a node of each connected sub-graph of G.

