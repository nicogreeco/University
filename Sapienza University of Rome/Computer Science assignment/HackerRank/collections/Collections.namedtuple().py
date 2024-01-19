from collections import OrderedDict
ord_dic = {}
n = int(input())
for a in range(n):
    lst = input().split()
    m = lst.pop(len(lst)-1)
    inpu = ' '.join([item for item in lst])
    if inpu in ord_dic:
        ord_dic[inpu] = int(m) + ord_dic[inpu]
    else:
        ord_dic[inpu] = int(m)
for k in ord_dic:
    print(k, ord_dic[k])


