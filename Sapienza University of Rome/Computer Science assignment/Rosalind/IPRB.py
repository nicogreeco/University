l = list(map(int, input().split()))
t = sum(l)
k = l[0]
m = l[1]
n = l[2]
# formula I have calculated to have prob of Dominant phenotype
# P(AA x __) + P(Aa x Aa)*(0.75) + P(Aa x aa)*(0.5)
# Probability to have each match times probability it gives a dominant phenotype
pAA = (k/t) + (k/(t-1)) - (k**2)/(t**2-t)
print(pAA)
pAa = (m/t)*((m-1)/(t-1))
print(pAa)
paa = (m*n/(t**2-t))*2
print(paa)
p = pAA + pAa*(0.75) + paa*(0.5)
print(p)