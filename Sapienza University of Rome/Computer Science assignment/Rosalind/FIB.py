
def fibonacci_of(n,k):
    cache = {0: 1, 1: 1} # in the gen zero we already have one pair of rabbits
    if n in cache:       # and after one month it reach repropductive age so
        return cache[n]  # month one still one pair

    cache[n] = fibonacci_of(n - 1,k) + fibonacci_of(n - 2,k)*k
    return cache[n]
    # just a fibonacci recursive function with implemented k values
n, k = map(int,input().split())
ll = [fibonacci_of(x, k) for x in range(n)]
print(*ll)