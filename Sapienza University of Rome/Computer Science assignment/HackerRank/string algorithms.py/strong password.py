def minimumNumber(n, password):
    lst = [0 for _ in range(4)]
    for a in password:
        if a.isupper() == True:
            lst[0] = 1
        if a.isnumeric() == True:
            lst[1] = 1
        if a.islower() == True:
            lst[2] = 1
        if not a.isalnum() == True:
            lst[3] = 1
    c = 0
    for a in lst:
        if a == 0:
            c += 1
    if c < (6 - len(password)):
        c = 6 - len(password)
    return c

