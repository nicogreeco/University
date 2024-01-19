def insertionSort2(n, arr):
    for i in range(1, n):
        count = 0
        while count < i:
            if arr[count] > arr[i]:
                temp = arr[i]
                for a in reversed(range(count,i)):
                    arr[a+1] = arr[a]
                arr[count] = temp
            else:
                count += 1
        print(*arr)
