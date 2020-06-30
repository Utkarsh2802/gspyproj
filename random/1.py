t=int(input())
for i in range(t):
    n,m,k=list(map(int,input().split()))
    numberofcards=int(n/k)
    ans=0
    if m<=numberofcards:
        print(m)
    else:
        l=[0 for i in range(k)]
        l[0]=numberofcards
        m-=numberofcards
        fill=int(m/(k-1))
        print(m,k)
        print(l[0],fill)
        for i in range(1,k):
            if i!=k-1:
                l[i]=fill
                m-=fill
            else:
                l[i]=m
        print(l[0]-max(l[1:]))