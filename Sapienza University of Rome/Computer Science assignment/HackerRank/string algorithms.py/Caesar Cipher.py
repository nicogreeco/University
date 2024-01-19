
def caesarCipher(s, k):
    ab = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    rot_s = ''
    for a in s:
        if a != '-':
            if a.isupper() == True:
                indx = ab.index(a.lower())
                if indx + k <= 25:
                    rot_s = F"{rot_s}{ab[indx+k].upper()}"
                else:
                    rot_s = F"{rot_s}{ab[indx+k-26].upper()}"       
                                    
            else:
                indx = ab.index(a)
                if indx + k <= 25:
                    rot_s = F"{rot_s}{ab[indx+k]}"
                else:
                    rot_s = F"{rot_s}{ab[indx+k-26]}"
        else:
            rot_s = F"{rot_s}-"
    return rot_s

print(caesarCipher(input(),int(input())))