f=open("input07.txt",'r')
l,q=list(map(int,f.readline().split()))
arr=[[0,0] for i in range(l+2)]
for i in range(q):
    a,b,k=list(map(int,f.readline().split()))
    arr[a][0]+=k
    arr[b][1]-=k
currmax=0
ans=0 
for i in range(1,l+2):
    ans+=(arr[i][0]+arr[i-1][1])
    if ans>=currmax:
        currmax=ans
print(currmax)
