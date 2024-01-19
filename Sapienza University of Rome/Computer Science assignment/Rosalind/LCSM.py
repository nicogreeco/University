def find_sub_in_list(substring, list):
    c = 0
    for a in list:
        if substring in a:
            c += 1
    if c == len(list):
        return True
    else:
        return False


f = open('Rosalind/rosalind_lcsm.txt').read()
list = list(f.split('>'))
n = 1
dnaseq = []
while n < len(list):
    list[n] = list[n].replace('\n', '')
    dnaseq.append(list[n][13:])
    n += 1

str = dnaseq.pop(0)

n = 1
m = 0
longer_seq = ''
while (m + n) < len(str):
    sub = str[m:m+n]
    if find_sub_in_list(sub,dnaseq):
        
        longer_seq = sub
        n += 1
    else:
        m += 1
print(longer_seq)