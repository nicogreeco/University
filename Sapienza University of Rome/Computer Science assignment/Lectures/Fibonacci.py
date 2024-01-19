
def fibo_1(n):
    print(f'Calculating {n}')
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo_1(n-1) + fibo_1(n-2)

''' creating function can be useful but it make the calculation much difficult, expetially
if we have self calling, it is related to how the compiler work. It essentially calculate back 
the same calculation each time, look to the calculating print'''

def fibo_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return
    else:
        fibo = 0 + 1
        n_2, n_1 = 1, 1
        for value in range(3,n+1):
            fibo = n_2 + n_1
            n_2 = n_1
            n_1 = fibo
        return fibo
    
''' a simple for loop is instead is less stresfull for the compiler '''

s = input('do u eant to use iterative (for) or recursive (def)?')
if s == 'def':
    print(fibo_1(int(input('n'))))
if s == 'for':
    print(fibo_2(int(input('n'))))

''' to avoid to each time calulate back all the numbers we cane sve the results in a dictionary'''

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
