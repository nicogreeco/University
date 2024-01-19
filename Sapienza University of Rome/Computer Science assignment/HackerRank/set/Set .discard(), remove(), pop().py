n = input()
s = set(map(int,input().split()))
for a in range(int(input())):
    c = input().split()
    if c[0] == 'remove':
        s.remove(int(c[1]))
    elif c[0] == 'discard':
        s.discard(int(c[1]))
    else:
        s.pop()
print(sum(s))
