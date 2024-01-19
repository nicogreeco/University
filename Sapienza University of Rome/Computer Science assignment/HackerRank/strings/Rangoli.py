def print_rangoli(size):
    trattini = '--'
    trattino = '-'
    lista = []
    s = '0 a b c d e f g h i j k l m n o p q r s t u v w x y z'
    alp = s.split(' ')
    for a in range(1,size+1):
        linea=''
        x = size - a
        for b in range(x):
            linea = F"{linea}{trattini}"
        left_sequence = ""
        letter_sequence = ""
        for b in range(a):
            y = size - b
            letter = alp[y]
            if b != (a-1):
            # letter = F"{trattino}{letter}"
                letter_sequence = F"{trattino}{letter}{letter_sequence}"
                left_sequence = F"{left_sequence}{letter}{trattino}"
            else:
                letter_sequence = F"{letter}{letter_sequence}"
        complete_line = F"{linea}{left_sequence}{letter_sequence}{linea}"
        lista.append(complete_line)
    for d in reversed(range(len(lista)-1)):
        lista.append(lista[d])
    for c in lista:
        print(c)   
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)