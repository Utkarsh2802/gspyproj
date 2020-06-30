t = int(input())

finale=2
def dist(s1, s2, length,tempo,finale):
    tempoo=list(tempo)
    count = 0
    for i in range(length):
        if s1[i] != tem[i]:
            count += 1
        else:
            tempoo[i]=s1[i]
    if count==2 and finale==2:
        tt=0
        finale=1
        for i in range(length):
            if s1[i] != s2[i] and tt==0:
                tt=1
                tempoo[i] = s1[i]
            elif tt==1 and s1[i]!=s2[i]:
                tempoo[i] = s2[i]

    tempo="".join(tempoo)
    return [count,tempo,finale]


for _ in range(t):
    finale=2
    n, m = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append(input())
    flag=0
    ans=""
    for i in range(m):
        ans+="z"
    ans=l[0]
    for i in range(n - 1):
        for j in range(i + 1, n):
            distance,ans,finale=dist(l[i], l[j], m, ans,finale)
            if distance<= finale:
                continue
            else:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        print(-1)
    else:
        print(ans)
