t=int(input())
import math
ll=[]

# method to print the divisors
def Divisors(n):
    # Note that this loop runs till square root
    i = 1
    while i <= math.sqrt(n):

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i):
                ll.append(i)
            else:
                # Otherwise print both
                ll.append(i)
                ll.append(n/i)
        i = i + 1


for i in range(t):
    #n=int(input())
    total,siz=list(map(int,input().split()))
    if total<=siz:
        print(1)
        continue
    ans=total
    Divisors(total)
    ll.sort(reverse=True)
    #print(ll)
    for i in ll:
        if i<=siz:
            ans=total/i
            break
    ll=[]
    print(int(ans))



