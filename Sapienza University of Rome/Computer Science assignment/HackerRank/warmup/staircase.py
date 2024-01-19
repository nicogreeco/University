def staircase(n):
    canc = '#'
    space = ' '
    lst = []
    for a in range(1,n+1):
            linel = ''
            liner = ''
            for b in range(a):
                liner = F"{liner}{canc}"
            for b in range(n-a):
                linel = F"{linel}{space}"
            line = F"{linel}{liner}"
            lst.append(line)
    for c in lst:
        print(c)