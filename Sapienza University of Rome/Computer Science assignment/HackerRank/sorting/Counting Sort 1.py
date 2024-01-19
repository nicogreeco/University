def countingSort(arr):
    
    lst = [0 for _ in range(100)]
    for a in arr:
        lst[a] += 1
    return lst
