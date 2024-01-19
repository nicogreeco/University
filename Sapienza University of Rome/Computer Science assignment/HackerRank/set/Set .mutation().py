n = input()
a = set(map(int,input().split()))
for l in range(int(input())):
    b = input().split()
    c = set(map(int,input().split()))
    if b[0] == 'intersection_update':
        a.intersection_update(c)
    elif b[0] == 'update':
        a.update(c)
    elif b[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(c)
    else:
        a.difference_update(c)
print(sum(a))