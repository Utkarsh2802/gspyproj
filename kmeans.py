import random
import math


def eucldist(p0, p1):
    dist = 0.0
    for i in range(0, len(p0)):
        dist += (p0[i] - p1[i]) ** 2
    return math.sqrt(dist)


def kmeans(k, datapoints):
    d = len(datapoints[0])
    print("d: ",d)
    Max_Iterations = 1000
    i = 0

    cluster = [0] * len(datapoints)
    print("Cluster: ",cluster)
    prev_cluster = [-1] * len(datapoints)
    print("Prev Cluster: ",prev_cluster)


    cluster_centers = []
    #choosing the cluster center depending on the k value ... randomly
    '''for i in range(0, k):
        new_cluster = []

        cluster_centers += [random.choice(datapoints)]'''
    #centers to be input by the user
    cluster_centers.append([2,4,6])
    cluster_centers.append([9,3,1])
    force_recalculation = False

    while (cluster != prev_cluster) or (i > Max_Iterations) or (force_recalculation):

        prev_cluster = list(cluster)
        print("Prev Cluster: ", prev_cluster," i: ",i)

        force_recalculation = False
        i += 1

        # Update Point's Cluster Allegiance
        for p in range(0, len(datapoints)):
            #basically for each data point
            min_dist = float("inf")

            # Check min_distance against all centers
            for c in range(0, len(cluster_centers)):
# so c goes from 0 1 2 3 and dist just gets the distance of a data point from each centroid and the outer for loop iterates over multiple data points
                dist = eucldist(datapoints[p], cluster_centers[c])
                print("Distance: between point",p+1,"center :",c+1,"is",dist)
                if dist < min_dist:
                    min_dist = dist
                    cluster[p] = c  # Reassign Point to new Cluster
            #print("and its cluster is now: ",cluster[p])

        # Update Cluster's Position
        for k in range(0, len(cluster_centers)):
            new_center = [0] * d
            members = 0
            for p in range(0, len(datapoints)):
                if cluster[p] == k:  # If this point belongs to the cluster
                    for j in range(0, d):
                        new_center[j] += datapoints[p][j]
                    members += 1

            for j in range(0, d):
                if members != 0:
                    new_center[j] = new_center[j] / float(members)

                else:
                    print("ERORRRRRRRRRRRRRRRRRRRRRRRRR")
                    new_center = random.choice(datapoints)
                    force_recalculation = True

            cluster_centers[k] = new_center
        print("New centers are: ",cluster_centers)

    print("Results =>")
    print("Clusters centers: ", cluster_centers)
    print("Iterations", i)
    print("Assignments", cluster)
    return cluster_centers


if __name__ == "__main__":
    datapoints = [(2, 4,6), (1,2,3), (6,4,2), (9,3,1),(3,5,8), (1,2,6)]
    k = 2
    center = kmeans(k, datapoints)
    #trained
    ip = datapoints
    maxx = float("inf")
    k=0
    c=0
    jj=0
    for i in center:
        if eucldist(i,ip[jj]) < maxx:
            maxx = eucldist(i,ip[jj])
            k=c
        jj+=1
        c+=1
    print("The input data point should be in cluster: ",k)
    print(eucldist((1.5,3.5),(2,10)))