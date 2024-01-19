def camelcase(s):
    c = 1
    for a in s:
        if a.isupper() == True:
            c += 1
    return c
camelcase(input())