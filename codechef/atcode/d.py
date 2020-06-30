n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
vis=[False for i in range(n)]
a=[]
start=curr=0
vis[0]=True
a.append(start)
flag=0
for i in range(k):
    curr=a[-1]+1
    if vis[arr[curr-1]-1]:
        a.append(arr[curr-1] - 1)
        flag=1
        break
    else:
        vis[arr[curr-1]-1]=True
        a.append(arr[curr-1]-1)
if flag==0:
    print(curr)
#now i have req cycle
if 5<6:
    count=0
    #print(a,"a")
    for i in range(len(a)):
        if a[i]==a[-1]:
            new=a[i:-1]
            #print(new,a[i:-1])
            break
        else:
            count+=1
    #print(len(new),new)
    #rint(count,"c")
    print(new[(k-count)%(len(new))]+1)
