n = input()
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happy = 0

for x in array:
    if x in a:
        happy += 1
    elif x in b:
        happy -= 1
print (happy)