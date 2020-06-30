t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    count=[1 for i in range(n)]
    arr.sort()
    for i in range(n):
        for j in range(i,n-1):
            if arr[j]>=arr[j+1]-2:
                count[i]+=1
            else:
                break
        for j in range(i,0,-1):
            if arr[j]<=arr[j-1]+2:
                count[i]+=1
            else:
                break
    #print(count)
    print(min(count),max(count))
