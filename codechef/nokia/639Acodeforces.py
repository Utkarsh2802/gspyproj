x, n = list(map(int,input().split()))
l=list(map(int,input().split()))

def seive(n):
    prime =[True]*(n + 1)
    p = 2
    while(p * p<= n):
        if(prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    allPrimes = [x for x in range(2, n)if prime[x]]
    return allPrimes
prime=seive(n)
#all primes till n
#print(prime)
def dis(x):
    return distinct_prime_array[l.index(x)]
def distPrime(arr, allPrimes):
    list1=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in allPrimes:
            if  arr[i]%j==0:
                list1[i]+=1
    return list1
distinct_prime_array=distPrime(l,prime)
#print(distinct_prime_array)
maxi=max(distinct_prime_array)
# now just store this like we normally do for range queries to optimize this (sliding window)
#make a maxarray
maxarray=[0 for i in range(len(distinct_prime_array))]
init=0
index=0
for i in sorted(l):
    if dis(i)==maxi:
        print(i)
        break
for i in range(x):
    if init<=distinct_prime_array[i]:
        init=distinct_prime_array[i]
        index=i

#initial index n value have nbeen calculated




