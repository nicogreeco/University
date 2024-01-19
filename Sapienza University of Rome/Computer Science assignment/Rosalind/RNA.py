s = open('Rosalind/rosalind_rna.txt').read()

c = 0

while c < len(s):
    if s[c] == 'T':
        s = s[:c] + 'U' + s[c+1:]
    c += 1
print(s)
