n = input()
a = set(map(int, input().split()))
m = input()
b = set(map(int, input().split()))

inter = list(a.difference(b))
inter += list(b.difference(a))
inter.sort()
print(inter)