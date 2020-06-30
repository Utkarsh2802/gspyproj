t=int(input())
for _ in range(t):
    l=[[] for i in range(100)]
    rang=[1,10**(int(input()))-1]
    dic={}
    for i in range(10000):
        qi,ri=list(input().split())
        for j in ri:
            dic[j]=0
        qi = int(qi)
        l[qi].append(ri)
    string=''.join(list(dic.keys()))
    #print(string)
    arr=[0,0,0,0,0,0,0,0,0,0]
    '''
    for i in range(8,0,-1):
        temp=string
        for j in l[i]:
            if j in temp:
                temp=temp.replace(j,'')
                #print("temp",'',temp)
        arr[i+1]=temp
        string=string.replace(temp,'')
        print(string)
    #to find 1
    print(arr)
    print(string)
    string ="TP"
    newdic ={}
    newdic[string[0]]=0
    newdic[string[1]]=0'''
    #print(arr)
    for tt in range(19,100,10):
        for i in l[tt]:
            for j in i:
                dic[j]+=1
        #print(dic.items())
        max_value = max(dic.values())  # maximum value
        max_key = ''.join([k for k, v in dic.items() if v == max_value])
        arr[int(tt/11)]=max_key
        dic[max_key]=-999999999999999
    '''
    if newdic[string[0]]>newdic[string[1]]:
        arr[1]=string[0]
        arr[0]=string[1]
    else:
        arr[0]=string[0]
        arr[1]=string[1]
    '''
    for i in list(dic.keys()):
        if i not in arr:
            arr[0]=i
            break
    #print(arr)
    print('Case #',_+1,': ',''.join(arr),sep="")
