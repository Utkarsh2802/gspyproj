import math
def solution(n):
    n=int(n)
    root=1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641573
    ans=((n*(n+1))/2)
    ans=math.floor(ans*(root))
    ans-=math.floor((n/2))
    print(math.floor(ans))
solution(input())