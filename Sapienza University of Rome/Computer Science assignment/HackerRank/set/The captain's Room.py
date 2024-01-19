n = int(input())
l = list(map(int, input().split()))
s = set(l)
captain_room = 0
for a in s:
    c = 0
    for b in range(len(l)):
        if l[b] == a:
            c += 1
            if c>1:
                break
    if c == 1:
        captain_room = a
print(captain_room)