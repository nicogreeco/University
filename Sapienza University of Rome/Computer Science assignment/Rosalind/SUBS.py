f = open('Rosalind/rosalind_subs.txt').read()
str, sub = f.split()
list = [] #list where i will save the location of substrings
m = len(sub)
n = 0

while n < (len(str)-m+1):
    r_frame = str[n:n+m]   # I set the reading frame equal to len of substring
    if r_frame == sub:     #when i found a substring i immediatly save position in the list
        list.append(n+1)   #n + 1 cause python gives index starting from 0
    n += 1
print(*list)