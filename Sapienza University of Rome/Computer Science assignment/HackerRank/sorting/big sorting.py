def bigSorting(unsorted):
    for i in range(len(unsorted)):
        unsorted[i] = int(unsorted[i])
    unsorted.sort()
    for i in range(len(unsorted)):
        unsorted[i] = str(unsorted[i])
    return unsorted