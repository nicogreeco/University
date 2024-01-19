N = int(input())
R=[]
for a in range(N):
    in_put=input().split()
    command=in_put[0]
    if command == "insert":
        R.insert(int(in_put[1]),int(in_put[2]))
    if command == "remove":
        R.remove(int(in_put[1]))
    if command == "append":
        R.append(int(in_put[1]))
    if command == "sort":
        R.sort()
    if command == "pop":
        R.pop()
    if command == "reverse":
        R.reverse()
    if command == "print":
        print(R)
