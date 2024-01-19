def countingSort(arr):
    lst = [0 for _ in range(20000)]
    for a in arr:
        lst[a] += 1
    c = 0
    sol = []
    while c < 20000:
        for a in range(lst[c]):
            sol.append(c)
        c += 1
    m = len(sol)//2
    return sol[m]
    

