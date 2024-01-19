my_lst=[5,2,4,6,1,4,2,6]
def divide(lst):
    if len(lst) == 1:
        print('one item only:', lst)
        return my_lst
    left = lst[0:len(lst)//2]
    right = lst[len(lst)//2:]
    divide(left)
    divide(right)
    return merge(left,right)

def merge(a, b):
    result = []
    pos_left = 0
    pos_right = 0
    while pos_right < len(b) and pos_left < len(a):
        if a[0]<b[0]:
            result.append(a[pos_left])
            pos_left += 1
        else:
            result.append(b[pos_right])
            pos_right += 1
    while pos_left < len(a):
        result.append(a[pos_left])
        pos_left += 1
    while pos_right < len(b):
        result.append(b[pos_right])
        pos_right += 1  
    return result
print(divide(my_lst))
    
    
