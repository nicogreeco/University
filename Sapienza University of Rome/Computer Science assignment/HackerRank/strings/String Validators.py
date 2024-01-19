s = input()

sol=[0,0,0,0,0]
for i in s:
    if i.isalnum() == True:
        sol[0]=1
    if i.isalpha() == True:
        sol[1]=1
    if i.isdigit() == True:
        sol[2]=1
    if i.islower() == True:
        sol[3]=1
    if i.isupper() == True:
        sol[4]=1
for a in sol:
    if a == 1:
        print(True)
    else:
        print(False)

