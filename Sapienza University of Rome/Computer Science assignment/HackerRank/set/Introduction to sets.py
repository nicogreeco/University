def average(array):
    # your code goes here
    sets = set(array)
    sum = 0
    for a in sets:
        sum = sum + a
    return sum/len(sets)
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)