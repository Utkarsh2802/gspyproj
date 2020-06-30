from collections import defaultdict
t=int(input())
for _ in range(t):
    n,q=list(map(int,input().split()))
    s=input()
    arr=defaultdict(lambda:-1)
    dic = defaultdict(lambda:0)
    for i in s:
        dic[i]+=1
        #arr[dic[i]]+=1
    for i in range(q):
        query=int(input())
        if arr[query]!=-1:
            print(arr[query])
        else:
            ans=0
            for temp in dic.values():
                if query>=temp:
                    continue
                ans+=temp-query
            print(ans)
            arr[query]=ans
        #for each query print the mmin size of the pending queue
    #print(dic)