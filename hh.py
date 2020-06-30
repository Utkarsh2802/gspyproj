t=int(input())
for _ in range(t):
    n=int(input())
    a=0
    b=0
    cnt=int(n/2)
    l=[]
    for i in range(1,n+1):
        l.append(2**i)
    fin=sum(l)
    #print(fin)
    a+=l[-1]
    cnt-=1
    for i in range(cnt):
        a+=l[i]
    print(abs(a-(fin-a)))