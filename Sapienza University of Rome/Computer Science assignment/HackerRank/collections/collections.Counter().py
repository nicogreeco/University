from collections import Counter
n = input()
X = Counter(input().split())
m = int(input())
cash = 0
for a in range(m):
 #a = number of tha shoes, b = price
    a, b = input().split()
    if X[a] != 0:
        X[a] -= 1
        cash += int(b)
print(cash)