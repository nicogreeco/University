def compareTriplets(a, b):
    sol = [0, 0]
    i = 0
    while i < 3:
        if a[i]>b[i]:
            sol[0] += 1
            i += 1
        elif a[i]<b[i]:
            sol[1] += 1
            i += 1
        else:
            i += 1
    return sol