t = int(input())
for a in range(t):
    n = input()
    A = set(map(int, input().split()))
    m = input()
    B = set(map(int, input().split()))
    if A.union(B) == B:
        print(True)
    else:
        print(False)