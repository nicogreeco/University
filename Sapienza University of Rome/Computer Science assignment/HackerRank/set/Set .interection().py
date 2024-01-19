n = input()
a = set(map(int,input().split()))
m = input()
b = set(map(int,input().split()))

print(len(a.intersection(b)))