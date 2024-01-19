def birthdayCakeCandles(candles):
    max = 0
    count = 1
    for a in candles:
        if a > max:
            count = 1
            max = a
        elif a == max:
            count += 1
    return count
