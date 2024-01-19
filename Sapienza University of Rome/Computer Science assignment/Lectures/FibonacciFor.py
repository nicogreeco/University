def fibo_1_2(n):
    cache = {}
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo_1_2(n-1) + fibo_1_2(n-2)
print((fibo_1_2(int((input())))))
