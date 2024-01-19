s,i = input().split()
i= int(i)
from itertools import combinations
sol = list(combinations(s,i))
sol.sort()
for a in range(1, i+1):
    for b in combinations(sorted(s), a):
        print(*b, sep='')