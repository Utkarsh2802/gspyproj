t=int(input())
for different in range(t):
    s=input()
    strr=""
    prev=-1
    for i in range(len(s)):
        if i==0 and int(s[i])!=0:
            #base case
            for _ in range(int(s[i])):
                strr+="("
            strr+=s[i]
            prev=int(s[i])
            continue
        elif i==0 and int(s[i])==0:
            strr+=s[i]
            prev=int(s[i])
            continue
        if int(s[i])>prev:
            for _ in range(int(s[i])-prev):
                strr+='('
            strr+=s[i]
        elif int(s[i])==prev:
            strr+=s[i]
        else:
            for _ in range(prev-int(s[i])):
                strr+=')'
            strr+=s[i]
        prev=int(s[i])

    for i in range(int(s[-1])):
        strr+=')'
    z="Case #"
    z+=str(different+1)
    z+=":"
    print(z,strr)