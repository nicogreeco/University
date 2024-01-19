from scipy.stats import binom # function to calculate prob of binomial distribution
k = 5 # generastion of intrest
n = 8 # n of AaBb that at least has to be in the pop
lista = [n for n in range(n,2**k+1)]
# binom.pmf(number of success, population, success probability)
# give an arrey as number of success it will calculate prob for each element in it
# so i can calculate the prob of at least n AaBb summing prob of n, n+1, ... k**2
p =sum(binom.pmf(lista,2**k,0.25))
print(p)