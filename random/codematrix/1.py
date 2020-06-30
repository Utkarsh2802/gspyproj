from collections import defaultdict
t=int(input())
for _ in range(t):
    prince,hurdle=list(map(int,input().split()))
	princearr = list(map(int, input().split()))
	hurdlearr=list(map(int, input().split()))
	check=max(princearr)
	maxpassed=-1
	for i in hurdlearr:
		if check>=i:
			if i>maxpassed:
				maxpassed=i
	for i in range(prince):
		if princearr[i]>=maxpassed:
			ans=i
			break
	print(ans)