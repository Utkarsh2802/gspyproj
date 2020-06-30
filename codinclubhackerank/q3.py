n,q=list(map(int,input().split()))
ans=0
matrix=[[0 for i in range(n+1)] for j in range(n+1)]
rowsum=[0 for i in range(n+1)]
for _ in range(q):
    strr=list(map(int,input().split()))
    tt=strr[0]
    if tt==2:
        i,j=strr[1:3]
        #invertbit
        if matrix[i][j]==0:
            matrix[i][j]=1
            rowsum[i]+=1
        else:
            matrix[i][j]=0
            rowsum[i]-=1
    elif tt==3:
        i=strr[1]
        rowsum[i]=n-rowsum[i]
        for z in range(n+1):
            matrix[i][z]=1-matrix[i][z]
        #invert in row i
    else:
        #tt=1
        ans=sum(rowsum)
        print(ans)