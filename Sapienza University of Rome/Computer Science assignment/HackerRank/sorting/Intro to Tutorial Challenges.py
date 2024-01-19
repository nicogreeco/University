def introTutorial(V, arr):
    n = 0
    while n < len(arr):
        if V == arr[n]:
            return n
            break
        else:
            n += 1