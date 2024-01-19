f = open('Rosalind/rosalind_gc.txt').read()
list = list(f.split('>'))
n = 1
dnaseq = {}
while n < len(list):
    list[n] = list[n].replace('\n', '')
    dnaseq[list[n][:13]] = list[n][13:]
    n += 1
# opened the txt file and create a dictonary with string label as key and 
# the dna sequence as value

# define so the function giving the CG content
def CGperc(string):
    dic = {'A':0, 'C':0, 'G':0, 'T':0}

    for a in string:
        if a == 'A':
            dic['A'] += 1
        elif a == 'T':
            dic['T'] += 1
        elif a == 'C':
            dic['C'] += 1
        elif a == 'G':
            dic['G'] += 1
    perc = (dic['C'] + dic['G'])/len(string)*100
    return perc


# substitute each dna string in the dictonary with its CG content
for a in dnaseq:
    dnaseq[a] = CGperc(dnaseq[a])

# find the biggest
st_name = ''
CG_content = 0
for a in dnaseq:
    if dnaseq[a] > CG_content:
        CG_content = dnaseq[a]
        st_name = a
print(st_name, '\n', CG_content)
