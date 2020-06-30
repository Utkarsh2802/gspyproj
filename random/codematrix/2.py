from collections import defaultdict
t=int(input())


def printPreorder(root):
    if root:
        # First print the data of node
        print(root,sep=" ",end=" ")

        # Then recur on left child
        printPreorder(dic[str(root)+'l'])

        # Finally recur on right child
        printPreorder(dic[str(root)+'r'])
for _ in range(t):
    temp=int(input())
    dic=defaultdict(lambda:0)
    for i in range(temp):
        root,left,right=list(map(int,input().split()))
        if i==0:
            rr=root
        dic[str(root)+'l']=left
        dic[str(root)+'r']=right
    #print(dic)
    printPreorder(rr)

