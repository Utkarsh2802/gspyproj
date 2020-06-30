t=int(input())
def complement(x):
    new=["0","b","1"]
    x=list(bin(x))
    for i in x[2:]:
        if i=="0":
            new+="1"
        else:
            new+="0"
    return "".join(new)
for _ in range(1,t+1):
    x,y=list(map(int,input().split()))
    if (x%2!=0 and y%2!=0) or (x%2==0 and y%2==0):
        print("Case #", _ , ": ","IMPOSSIBLE", sep="")
        break
    #keep the even number as it is
    #solve for the odd number
    if x>=0:
        xneg=False
    else:
        xneg=True
    if y>=0:
        yneg=False
    else:
        yneg=True
    X=abs(x)
    Y=abs(y)
    x=X
    y=Y
    switch=False
    if y%2==0:
        x,y=y,x
        switch=True
    if x%2==0:
        compx=complement(x)#2**(len(bin(x))-2)-x-1
        yy=bin(y)
        diff=abs(len(yy)-len(compx))
        tempstr="1"*(diff)
        if len(yy)>len(compx):
            #print("h")
            compx=compx.replace("0b",tempstr)
        else:
            #print("hh")
            compx=compx.replace("0b","")
        #print(compx)
        answer1=int((int(compx,2)+y)/2)
        answer2=answer1-y
        print(answer1,answer2,x)
    a1=bin(answer1)
    a2=bin(answer2)
    xx=bin(x)
    ans=""
    i=1
    if answer1>x:
        sss="0"*(len(a1)-len(xx))
        res = list(xx)
        res.insert(2, sss)
        res = ''.join(res)
        xx=res
        sss = "0" * (len(a1) - len(a2))
        res = list(a2)
        res.insert(2, sss)
        res = ''.join(res)
        a2 = res
    else:
        sss = "0" * (len(xx) - len(a1))
        res = list(a1)
        res.insert(2, sss)
        res = ''.join(res)
        a1 = res
        sss = "0" * (len(xx) - len(a2))
        res = list(a2)
        res.insert(2, sss)
        res = ''.join(res)
        a2 = res
    while(True):
        if not switch:
            if xx[-i]=='b':
                break
            if a1[-i]=='1':
                if yneg==False:
                    ans+="N"
                else:
                    ans+="S"
            elif a2[-i]=='1':
                if yneg==False:
                    ans+="S"
                else:
                    ans+="N"
            else:
                if xneg==False:
                    ans+="E"
                else:
                    ans+="W"
            i+=1
        else:
            if xx[-i]=='b':
                break
            if a1[-i]=='1':
                if xneg==False:
                    ans+="E"
                else:
                    ans+="W"
            elif a2[-i]=='1':
                if xneg==False:
                    ans+="W"
                else:
                    ans+="E"
            else:
                if yneg==False:
                    ans+="N"
                else:
                    ans+="S"
            i+=1
    print("Case #", _, ": ", ans, sep="")



'''4
2 3
-2 - 3
3 0
-1 1

Case  # 1: SEN
Case  # 2: NWS
Case  # 3: EE
Case  # 4: IMPOSSIBLE'''