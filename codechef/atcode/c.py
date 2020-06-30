num_books,m,min_understanding=list(map(int,input().split()))
info=[]
for _ in range(num_books):
    arr=list(map(int,input().split()))
    info.append(arr)
#print(info)
from itertools import combinations
l=[i for i in range(1,num_books+1)]
new=[]
for i in range(1,num_books+1):
    new.append(list(combinations(l,i)))
#print(new)
def add(l1,l2):
    faltu=[0 for i in range(len(l1))]
    #print(len(l1),len(l2),"fds")
    #print(l1,l2,"daa")
    for i in range(len(l1)):
        faltu[i]=l1[i]+l2[i]
    return faltu
def check(temp):
    #print(temp,len(temp))
    ans=[0 for i in range(m+1)]
    for i in range(len(temp)):
        ans=add(ans,info[temp[i]-1])
    for i in range(1,len(ans)):
        if ans[i]>=min_understanding:
            continue
        else:
            return 999999999
    return ans[0]
tempo=[]
for i in new:
    for j in i:
        tempo.append(check(j))
if min(tempo)==999999999:
    print(-1)
else:
    print(min(tempo))#arr[0] would be the price of that book