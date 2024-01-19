n = int(input())
k = int(input())

def fac(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

print(fac(n)/fac(n-k)%1000000)