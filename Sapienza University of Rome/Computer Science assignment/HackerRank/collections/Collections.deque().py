from collections import deque
n = int(input())
d = deque()
for a in range(n):
    lst = input().split()
    inpu = lst[0]
    if len(lst) > 1:
        m = int(lst[1])
    if inpu == 'append':
        d.append(int(m))
    elif inpu == 'appendleft':
        d.appendleft(int(m))
    elif inpu == 'pop':
        d.pop()
    else:
        d.popleft()
print(*d)
