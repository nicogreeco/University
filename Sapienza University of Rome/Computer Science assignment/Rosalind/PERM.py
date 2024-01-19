n = int(input())

from itertools import permutations

perm = list(permutations(list(range(1,n+1))))

print(len(perm))
for a in perm:
    print(*a)