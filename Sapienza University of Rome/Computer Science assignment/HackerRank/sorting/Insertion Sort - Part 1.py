def insertionSort1(arr):
    n = len(arr)
    num = arr[n - 1]
    for j in range(len(arr)-2, -1, -1):
        if arr[j] < num:
            arr[j+ 1] = num
            break
        arr[j+1] = arr[j]
    if arr[0] > num:
        arr[0] = num
    print(arr)
       