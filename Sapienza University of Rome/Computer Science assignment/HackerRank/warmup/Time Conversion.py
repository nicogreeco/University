def timeConversion(s):
    d = s[8:]
    s = s[:8]
    s = s.split(':')
    if d == 'PM' and s[0] != '12':
        s[0] = int(s[0])
        s[0] = str(s[0] + 12)
    if d == 'AM' and s[0] == '12':
        s[0] = '00'
    sol = F"{s[0]}:{s[1]}:{s[2]}"
    return sol

