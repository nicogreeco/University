inpu = input().split()
inpu[1]= int(inpu[1])

from itertools import permutations

sol = list(permutations(inpu[0], inpu[1]))
sol.sort()
for a in sol:
    print(*a, sep='')