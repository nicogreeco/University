s_1 = set(map(int, input().split()))
n = int(input())
sol = True
for a in range(n):
    s_2 = set(map(int, input().split()))
    if not s_2.issubset(s_1):
        sol = False
    if len(s_2) >= len(s_1):
        sol = False
print(sol) 