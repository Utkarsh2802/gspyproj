from fractions import Fraction as f

l = [[0, 1, 0, 0, 0, 1],
     [4, 0, 0, 3, 2, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]
#l = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# using an adjacency list would have been more efficient but since the graph is small it wont make much of a difference
def solve(l):
    connected = [[] for temp in range(len(l[0]))]
    terminalstate = [False for temp1 in range(len(l[0]))]
    sumofrow = [0 for temp2 in range(len(l[0]))]
    for i in range(len(l[0])):
        for j in range(len(l[0])):
            sumofrow[i] += l[i][j]  # to easily calculate the probabilities
        if sumofrow[i] == 0:
            terminalstate[i] = True  # so that we can easily check later whether a state is terminal or not

    recur = [0 for temp4 in range(len(l[0]))]
    realprob = [0 for temp5 in range(len(l[0]))]
    ansprob = [0 for temp6 in range(len(l[0]))]

    def gcd(a,b):
        if a==0:
            return b
        return gcd(b%a,a)

    def lcm(a, b):
        return (a * b) / gcd(a, b)

    def util(start, visited, probability, recur, realprob):
        visited[start] = True
        realprob[start] += probability
        for i in range(len(l[start])):
            if visited[i] == False and l[start][i] != 0:
                recur, realprob = util(i, visited, probability * (f(l[start][i], sumofrow[start])), recur, realprob)
            elif visited[i] == True and l[start][i] != 0:
                if terminalstate[i]:
                    realprob[i] += probability * f(l[start][i], sumofrow[start])
                else:
                    recur[i] += probability * f(l[start][i], sumofrow[start])
        #print(probability, start)
        #print(recur, realprob)
        return recur, realprob


    def dfs2(initial, start, visited):
        visited[start] = True
        connected[initial].append(start)
        for i in range(len(l[start])):
            if visited[i] == False and l[start][i] != 0:
                dfs2(initial, i, visited)


    def dfs():
        probability = f(1)
        visited = [False for i in range(len(l[0]))]
        util(0, visited, probability, recur, realprob) #main cauclation starter
        visited = [False for i in range(len(l[0]))]
        for i in range(len(l[0])):
            visited = [False for j in range(len(l[0]))]
            dfs2(i, i, visited)


    dfs()
    #print(connected)
    #print("#######################")
    #print(realprob)
    # calculation of the final probabilities are done below
    for i in range(0, len(l[0])):
        if recur[i] != 0:
            for j in connected[i]:
                ansprob[j] += (realprob[j] * recur[i] / (
                            1 - recur[i]))  # edited this line and added the below line press ctrl+z tomorrow
        ansprob[i] += realprob[i]
    maxdenominator = -1
    #print(ansprob)
    #ansprob.append(f(1,10))
    # this just gets the max denominator but remmeber to take gcd tomorrow to get the correct ans in case of(1/3,7/22)type of fractions and get 66 as the common denominator
    for i in range(1,len(ansprob)-1):
        maxdenominator=lcm(ansprob[i].denominator,ansprob[i+1].denominator)
    for i in range(1, len(ansprob)):
        if ansprob[i].denominator != maxdenominator:
            tobedividedby = int(maxdenominator / ansprob[i].denominator)
            ansprob[i] *= (f(tobedividedby, 1))
    final = []
    for i in range(len(ansprob)):
        if terminalstate[i]:
            final.append(ansprob[i].numerator)
    final.append(int(maxdenominator))
    return final
print(solve(l))