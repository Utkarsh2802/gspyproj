t=int(input())
import math
for i in range(t):
    n,k=list(map(int,input().split()))
    s=input()
    oneindex=[]
    count=0
    for j in range(n):
        if s[j]=='1':
            oneindex.append(j)
    if len(oneindex)<2:
        if len(oneindex)==0:
            print(math.ceil(n/(k+1)))
            continue
        else:
            print(math.floor(n / (k + 1)))
            continue
    for j in range(len(oneindex)):
        if j==len(oneindex)-1:
            if abs(n-oneindex[j]+oneindex[0])>=2*k+1:
                count+=1
            continue
        if abs(oneindex[j]-oneindex[j+1])>=2*k+1:
            count+=1
    print(count)
