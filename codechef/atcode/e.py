n=int(input())
o=[]
c=[]
oa=[]
ca=[]
for i in range(n):
    s=input()
    open=0
    closed=0
    l=[]
    for j in s:
        if j==')' and len(l)!=0:
            l.pop()
            closed-=1
        elif j==')':
            open+=1
        elif j=='(':
            closed+=1
            l.append('(')
    oa.append(closed)
    ca.append(open)
    print(open,closed)
    o.append(open)
    c.append(closed)
print(o,c)
if sum(o)==sum(c):
    print("Yes")
else:
    print("No")