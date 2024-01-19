def miniMaxSum(arr):
    
    max = 0
    min = 0
    arr.sort()
    for a in range(1,5):
        max += arr[a]
    for a in range(4):
        min += arr[a]
    print( min, max)
