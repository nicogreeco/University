from itertools import product
abb = list(input().split())
n = int(input())
perm = [p for p in product(abb, repeat=n)]

def come_first(a, b):
    ab = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
    ab = list(ab.split(', '))
    dic = {ab[n] : n for n in range(len(ab))}   # creastion af o dic having letters as keys
    for indx in range(len(a)):                  # and as values numbers related to alphabetic order 
        if dic[a[indx]] > dic[b[indx]]:
            
            return False
        elif dic[a[indx]] == dic[b[indx]]:         # function that is treu if the first element
            continue                               # come before the second in alphabetical order
        else:    
            
            return True
        

def find_firstone(list):
    first = 'ZZZZZZZZZZ'
    for element in list:
        if come_first(element,first):     # funtion taking as input a list of string or lists
            first = element               # and returning the fisrt element in alphabeit order
    return first

for a in range(len(perm)):
    smaller = find_firstone(perm)
    perm.remove(smaller)
    smaller = ''.join(smaller)        # genereting the solution of th problem
    print(smaller)