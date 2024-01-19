from itertools import combinations_with_replacement
s,i = input().split()
i= int(i)
s = list(s)
s.sort()
sol = list(combinations_with_replacement(s,i))
for a in sol:	
    print(*a, sep='')