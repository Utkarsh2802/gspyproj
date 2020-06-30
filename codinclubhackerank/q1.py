t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    #print(max(min(a,b)*2,max(a,b))**2)
    l.sort()
    odd=0
    for j in range(n):
        if l[j]%2!=0:
            odd+=1
    even =n-odd
    diff1=0
    j=0
    for z in range(n-1):
        if l[j+1]-l[j]==1:
            diff1+=1
            j+=1
        j += 1
        if j>=n-1:
            break

    #print(even,odd,diff1)
    if even%2==0 and odd%2==0:
        print("YES")
        continue
    else:
        flag=0
        for zz in range(1,diff1+1):
            if (even-zz)%2==0 and (odd-zz)%2==0:
                print("YES")
                flag=1
            break
        if flag==1:
            continue
    print("NO")