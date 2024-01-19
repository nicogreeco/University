def theLoveLetterMystery(s):
    c = 0
    for a in range(len(s)//2):
        c += abs(ord(s[a]) - ord(s[len(s)-1-a]))
    return c