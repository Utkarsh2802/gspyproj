t= int(input())
def flip(curr):
    if curr=='J':
        return 'C'
    else:
        return 'J'
def overlap(l1,l2):
    a,b=l1
    c,d=l2
    if b<=c or d<=a:
        return False
    else:
        return True
def insert(i,dic):
    if tuple(i) in dic.keys():
        dic[tuple(i)]=dic[tuple(i)]+flip(dic[tuple(i)])
for _ in range(t):
    n_activities=int(input())
    l=[]
    og_array=[]
    dic={}
    curr='J'
    answer="IMPOSSIBLE"
    for i in range(n_activities):
        start,end = list(map(int,input().split()))
        og_array.append([start,end])
    l=list(og_array)
    l.sort()
    cnt=0
    dic[tuple(l[0])]='J'
    for i in range(1,len(l)-1):
        if l[i][0]<l[i-1][1]:
            if l[i][1]>l[i+1][0]:
                if l[i+1][0]<l[i-1][1]:
                    cnt=2
                    break
                else:
                    if tuple(l[i]) in dic.keys():
                        dic[tuple(l[i])] = dic[tuple(l[i])] + flip(dic[tuple(l[i])])
                    else:
                        if len(dic[tuple(l[i-1])])==1:
                            dic[tuple(l[i])]=flip(dic[tuple(l[i-1])])
                        else:
                            dic[tuple(l[i])]=flip(dic[tuple(l[i-1])][1])
            else:
                if tuple(l[i]) in dic.keys():
                    dic[tuple(l[i])] = dic[tuple(l[i])] + flip(dic[tuple(l[i])])
                else:
                    if len(dic[tuple(l[i - 1])]) == 1:
                        dic[tuple(l[i])] = flip(dic[tuple(l[i - 1])])
                    else:
                        dic[tuple(l[i])] = flip(dic[tuple(l[i - 1])][1])
        else:
            if tuple(l[i]) in dic.keys():
                dic[tuple(l[i])] = dic[tuple(l[i])] + flip(dic[tuple(l[i])])
            else:
                if len(dic[tuple(l[i - 1])]) == 1:
                    dic[tuple(l[i])] = flip(dic[tuple(l[i - 1])])
                else:
                    dic[tuple(l[i])] = flip(dic[tuple(l[i - 1])][1])
    #print(dic,l,og_array)
    if cnt==2:
        answer="IMPOSSIBLE"
    else:
        answer=""
        if tuple(l[-1]) in dic.keys():
            dic[tuple(l[-1])] = dic[tuple(l[-1])] + flip(dic[tuple(l[-1])])
        else:
            if overlap(l[-1],l[-2]):
                dic[tuple(l[-1])] = flip(dic[tuple(l[-2])])
            else:
                dic[tuple(l[-1])] = dic[tuple(l[-2])]
        '''for i in range(len(l)):
            dic[tuple(l[i])]=curr
            curr=flip(curr)
        print(l,dic)'''
        for i in range(0,len(og_array)):
            if len(dic[tuple(og_array[i])])>1:
                answer+=dic[tuple(og_array[i])][0]
                dic[tuple(og_array[i])]=dic[tuple(og_array[i])][1]
            else:
                answer += dic[tuple(og_array[i])]
        #logic:if the next interval doesnt overlap with the prev then output the same letter else flip the letter
    #output starts here...
    output="Case #"
    output+=str(_+1)
    output+=":"
    print(output,answer)