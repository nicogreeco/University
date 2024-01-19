def swap_case(s):
    l=list(s)
    for a in range(len(l)):
        if l[a].isupper() != True:
            l[a]=l[a].upper()
        elif l[a].isupper() == True:
            l[a]=l[a].lower()
    sol=''
    for a in l:
        sol=F"{sol}{a}"
    return sol

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)