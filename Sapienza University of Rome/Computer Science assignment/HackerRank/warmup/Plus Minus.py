def plusMinus(arr):
    magg = 0
    mino = 0
    zero = 0
    for i in arr:
        if i>0:
            magg += 1
        elif i < 0:
            mino += 1
        else:
            zero += 1
    print(round(magg/len(arr), 6))
    print(round(mino/len(arr), 6))
    print(round(zero/len(arr), 6))        
