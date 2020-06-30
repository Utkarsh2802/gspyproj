class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s)==0 and (len(p)==0 or p=='*'):
            return True
        dp=[[0]*(len(s)+1) for i in range(len(p)+1)]
        dp[0][0]=1
        s=s.split('*')
        for i in s:
            str.find()
            index=p.find(s,0,len(p))
        return dp[len(p)][len(s)]
Sol=Solution()
def merge(s1,s2):
    test_list1=list(s1)
    test_list2=list(s2)
    temp = (i for i in range(len(test_list2), 0, -1) if test_list2[:i] == test_list1[-i:])
    temp2 = next(temp, 0)
    res = test_list1 + test_list2[temp2:]
    return "".join(res)
def check(plist):
    maxlen=0
    currmax=""
    maxlen2=0
    currmax2=""
    fluke=[]
    for i in plist:
        ww=i.split("*")
        if len(ww)>maxlen2:
            maxlen2=len(ww)
        fluke.append(ww)
    for i in fluke:
        while(len(i)!=maxlen2):
            i.append("")
    r=0
    c=0
    match=""
    #print(fluke)
    while(True):
        while(True):
            if len(fluke[c][r])>len(currmax):
                currmax=fluke[c][r]
            c+=1
            if c==len(fluke):
                break
        match=merge(match,currmax)
        currmax=""
        c=0
        r+=1
        if r==maxlen2:
            break
    #print(match)
    for _ in range(len(plist)):
        if Sol.isMatch(match,plist[_]):
            pass
        else:
            #print(plist[_])
            return '*'
    return match
t=int(input())
for _ in range(t):
    l=[]
    __=int(input())
    for temp in range(__):
        l.append(input())
    print("Case #",_+1,": ",check(l),sep="")
