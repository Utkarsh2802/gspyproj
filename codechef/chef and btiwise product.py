t=int(input())
for i in range(t):
    x,y,l,r=list(map(int,input().split()))
    ans=r
    for i in range(40,0,-1):
        if l<=2**i<=r:
            ans=2**i-1
            break
    print(ans)
