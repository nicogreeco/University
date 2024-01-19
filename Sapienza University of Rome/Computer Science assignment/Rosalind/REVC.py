s = ''
f = open('Rosalind/rosalind_revc.txt').read()

for a in f:
    b = ''
    if a == 'A':
        b = 'T'
    elif a == 'T':
        b = 'A'
    elif a == 'C':
        b = 'G'
    elif a == 'G':
        b = 'C'
    s = F"{b}{s}"

print(s)