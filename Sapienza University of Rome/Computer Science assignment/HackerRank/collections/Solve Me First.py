from collections import defaultdict
n, m = map(int, input().split())
A = []
B = []
for a in range(n):
    A.append(input())
for b in range(m):
    B.append(input())
sol = defaultdict(list)



for i in range(n):
    sol[A[i]].append(i+1)


for i in B:
    if i in sol:
        print(*sol[i])
    else:
        print(-1)