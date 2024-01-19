''' list of n elemets
scan the list and pick the loweast/biggest and move it to the first position
'''
b=[]
c = [8,5,9,3,1,6]
def find_max(myList):
    n=0
    max_index=0
    for a in range(len(myList)):
        if myList[a] > n:
            n = myList[a]
            max_index=a
    return n,max_index
def sort(x):
    for a in range(len(x)):
        max_value, max_index = find_max(x)
        del x[max_index]
        b.append(max_value)
    print(b)

# to swap simultaneusly two values of a list:
c[0],c[3]=c[3],c[0]
print(c)


    
