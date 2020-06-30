t=int(input())

for _ in range(t):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(input())
    val=0
    for i in range(n-1):
        for j in range(n-1):
            if l[i][j]=='1':
                if l[i][j+1]=='0' and l[i+1][j]=='0':
                    val=1
                if val==1:
                    break
        if val==1:
            break
    if val==1:
        print("NO")
    else:
        print("YES")


