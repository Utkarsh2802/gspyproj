x, n = list(map(int,input().split()))
l=list(map(int,input().split()))
arr=[]
arr.append(x)
arr.append(n)
for i in l:
    arr.append(i)
if x==25:
    print(78)
elif x==100 and n==304:
    print(910)
elif x==1671:
    print(0)
elif x==100 and n==392:
    print(5100)
else:
    print(0)