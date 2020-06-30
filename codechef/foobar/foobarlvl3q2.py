def solution(l):
    n=len(l)
    number_of_prev_div_ele=[0 for i in range(n)]
    for i in range(n):
        for j in range(0,i):
            if l[i]%l[j]==0:
                number_of_prev_div_ele[i]+=1
    #print(number_of_prev_div_ele)
    ans=0
    for i in range(n):
        for j in range(0,i):
            if l[i]%l[j]==0:
                ans+=number_of_prev_div_ele[j]
    return ans
l=[1,2,3,4,5,6]
print(solution(l))
'''
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            temp=[]
            temp.append(l[k])
            temp.append(l[j])
            temp.append(l[i])
            temp.sort()
            if temp[2]%temp[1]==temp[1]%temp[0]==0:
                count+=1
print(count)'''