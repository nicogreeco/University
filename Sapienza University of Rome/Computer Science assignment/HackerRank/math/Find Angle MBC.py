AB = int(input())
BC = int (input())
import math
tmp = (AB*AB)+(BC*BC)
AC = math.sqrt(tmp)
BM = AC/2
BN = BC/2
B = math.degrees(math.acos(BN/BM))
print(str(round(B))+chr(176))