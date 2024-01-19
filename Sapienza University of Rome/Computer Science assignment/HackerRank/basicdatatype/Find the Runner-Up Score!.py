n = int(input())
arr = map(int, input().split())
l=list(arr)
l.sort()
l=list(dict.fromkeys(l))
rnp=l[len(l)-2]
print(rnp)