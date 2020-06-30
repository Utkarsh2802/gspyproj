def solution(l):
    if len(l)==1:
        return max(0,str(l[0]))
    pos=[]
    neg=[]
    for i in l:
        if i<0:
            neg.append(i)
        elif i>0:
            pos.append(i)
    product=0
    if len(pos)==0 and len(neg)<=1:
        return 0
    else:
        product=1
    for i in pos:
        product*=i
    if len(neg)%2==0:
        for i in neg:
            product*=i
    else:
        for i in sorted(neg)[:-1]:
            product*=i
    return str(product)
l=[-3,0]
print(solution(l))