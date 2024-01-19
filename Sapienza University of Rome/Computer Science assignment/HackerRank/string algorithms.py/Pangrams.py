def pangrams(s):
    ab = set('a b c d e f g h i j k l m n o p q r s t u v w x y z'.split())
    for a in s.lower():
        if a != ' ':
            ab.discard(a)
    if len(ab) == 0:
        return 'pangram'
    else:
        return 'not pangram'
print(pangrams(input()))
