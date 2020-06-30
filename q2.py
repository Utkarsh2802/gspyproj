t=int(input())
for _ in range(t):
    n=0
    w=0
    e=0
    s=0
    pos=[1,1]
    string=input()
    stack=[]
    for i in string:
        temp=""
        if i.isdigit():
            if len(stack)!=0:
                stack.append(int(i)*stack[-1])
            else:
                stack.append(int(i))
            continue
        if i == ')':
            stack.pop()
            continue
        if i != '(' and len(stack)!=0:
            #it means this is a lettter
            times=stack[-1]
        else:
            times=1
        if i=='E':
            e+=times
        elif i=='W':
            w+=times
        elif i == "N":
            n+=times
        elif i == "S":
            s+=times
    #print(n,s,e,w)
    pos[0]+=(s-n)
    pos[1]+=(e-w)
    if pos[0]<1:
        pos[0]+=1000000000**100000
    if pos[0]>100000000:
        pos[0]%=1000000000
        if pos[0]==0:
            pos[0]=1000000000
    if pos[1]<1:
        pos[1]+=1000000000**100000
    if pos[1]>100000000:
        pos[1]%=1000000000
        if pos[1]==0:
            pos[1]=1000000000

    print("Case #", _ + 1, ": ", pos[1]," ",pos[0], sep="")

