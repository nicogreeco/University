f = open('Rosalind/rosalind_revp.txt').read()   # prepare the input
f = f = f[14:].replace('\n', '')



def is_reverse_pal(sub):        # creation of the functioin that check for
    b = ''
    complementary = ''          # palindromic revers
    for a in sub:
        if a == 'A':            
            b = 'T'
        elif a == 'T':
            b = 'A'
        elif a == 'C':
            b = 'G'
        elif a == 'G':
            b = 'C'
        complementary = F"{b}{complementary}"
    return complementary == sub


n = 4
m = 0
sol = []
reverse_seq = ''
while n < 13:
    m = 0                             # i span the entire sequence looking for palindromic
    while (m + n) <= len(f):        # reversed sequences of different lenght, from
        sub = f[m:m+n]              # from 4 to 12, adding them to the solution list
        if is_reverse_pal(sub):    
            sol.append((m+1, n))
            m += 1
        else:
            m += 1
    n += 1

for a in sol:
    print(*a)




