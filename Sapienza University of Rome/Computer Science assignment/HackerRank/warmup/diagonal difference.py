from _typeshed import SupportsItemAccess


def diagonalDifference(arr):
    c = 0
    l_arr = []
    r_arr = []
    for j in range(len(arr)):
        l_arr.append(arr[c][c])
        c += 1
    c = 0
    k = len(arr) - 1
    for j in range(len(arr)):
        r_arr.append(arr[c][k])
        c += 1
        k -= 1
    sol = sum(l_arr)-sum(r_arr)
    return abs(sol)
