def quickSort(arr):
    p = arr[0]
    l = []
    e = [p]
    r = []
    for i in range(1,len(arr)):
        if arr[i] > p:
            r.append(arr[i])
        elif arr[i] < p:
            l.append(arr[i])
        else:
            e.append(arr[i])
    return l + e + r
