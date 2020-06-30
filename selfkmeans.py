import math
import random
def euclidist(p1,p2):
    dist=0
    for i in range(len(p2)):
        dist+=(p1[i]-p2[i])**2
    return math.sqrt(dist)
datapoints = [[1,2],[3,4],[1.3,2.5]]#list(map(int,input().split()))
k = int(input("Enter the number of clusters"))
#choose the centers randomly
forcerecalc = False
centers = [0]*k
for i in range(0,k):
    centers[i]=random.choice(datapoints)
prev_center = list(centers)
max_iter = 10000
iter = 0
while prev_center!=centers or iter>1000 or forcerecalc:
    iter+=1
    cluster=[0]*len(datapoints)
    for i in range(0,len(datapoints)):
        tempdist = float("inf")
        for j in range(k):
            if(euclidist(datapoints[i],centers[j])<tempdist):
                #tempdist=euclidist(datapoints[i],centers[j])
                cluster[i]=j
    #now we have classified each n every datapoint
    #now we have to update the centers
    #so we take mean of the points belonging to a particular cluster
    for i in range(0,k):
        newcenter=[0]*len(datapoints[0])
        members=0
        for j in range(0,len(datapoints)):
            if(cluster[j]==i):
                for z in range(0,len(datapoints[0])):
                    newcenter[z]+=datapoints[j][z]
                members+=1
        if members!=0:
            for z in range(0,len(datapoints[0])):
                newcenter[z]=newcenter[z]/members
        else:
            newcenter=random.choice(datapoints)
            forcerecalc = True
        cluster[i]=newcenter






