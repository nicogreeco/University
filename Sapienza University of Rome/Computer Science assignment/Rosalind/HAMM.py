f = open('Rosalind/rosalind_hamm.txt').read()
s,t = f.split()
n = 0
distance = 0
while n < len(s):
    if s[n] != t[n]:
        distance += 1
    n += 1
print(distance)