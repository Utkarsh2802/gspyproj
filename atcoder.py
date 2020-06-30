t=int(input())
for _ in range(1,t+1):
    x,y,path=list(input().split())
    x=int(x)
    y=int(y)
    finalpos=[x,y]
    currpos=[0,0]
    dir={'N':[0,1],"S":[0,-1],"E":[1,0],"W":[-1,0]}
    #dir2 = {'N': [0, 1], "S": [0, 1], "E": [1, 0], "W": [1, 0]}
    count=0
    flag=0
    ll=[0 for temp in range(len(path))]
    k=0
    for i in path:
        finalpos[0]+=dir[i][0]
        finalpos[1] += dir[i][1]
        ll[k]=list(finalpos)
        k+=1
    #print(ll)
    for j in range(0,len(ll)):
        time=0
        time+=abs(ll[j][0])+abs(ll[j][1])
        #print(time,ll[j],j)
        if j+1>=time:
            flag=1
            print("Case #",_,': ',j+1,sep="")
            break
        else:
            continue
    if flag==0:
        print("Case #",_,': ',"IMPOSSIBLE",sep="")