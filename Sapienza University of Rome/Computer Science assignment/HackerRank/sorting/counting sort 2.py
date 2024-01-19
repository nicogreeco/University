def countingSort(arr):
    lst = [0 for _ in range(100)]
    for a in arr:
        lst[a] += 1
    c = 0
    sol = []
    while c < 100:
        for a in range(lst[c]):
            sol.append(c)
        c += 1

    return sol

