from fractions import Fraction as f
import numpy as np

# Reading order of matrix


l = [[21321, 123, 3112, 31112, 123, 1],
     [0, 0, 0, 0, 0, 0],
     [1, 1231212, 412321, 23213, 0, 0],
     [213, 0, 61, 0, 45, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]


def inversecalc(l):
    n = len(l[0])
    a = [[0 for temp in range(2 * n)] for temp1 in range(n)]

    for i in range(n):
        for j in range(n):
            a[i][j] = f(l[i][j])
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j + n] = f(1, 1)
            else:
                a[i][j + n] = f(0, 1)
    for i in range(n):
        for j in range(n):
            if i != j:
                r = f(a[j][i]) / f(a[i][i])
                for k in range(2 * n):
                    a[j][k] = a[j][k] - r * a[i][k]

    for i in range(n):
        d = a[i][i]
        for j in range(2 * n):
            a[i][j] = a[i][j] / d

    inversematrix = [[] for temp2 in range(n)]
    for i in range(n):
        for j in range(n, 2 * n):
            inversematrix[i].append(a[i][j])
    return inversematrix
def matmul(A,B):
    res=np.dot(A,B).tolist()
    return res
def solve(l):
    connected = [[] for temp in range(len(l[0]))]
    number_of_terminal_states=0
    number_of_non_terminal_states=0
    terminalstate = [False for temp1 in range(len(l[0]))]
    sumofrow = [0 for temp2 in range(len(l[0]))]
    ordering = []
    for i in range(len(l[0])):
        for j in range(len(l[0])):
            sumofrow[i] += l[i][j]  # to easily calculate the probabilities
        if sumofrow[i] == 0:  # make this 1 for detecting self loop  if 0 doesn't work
            terminalstate[i] = True
            number_of_terminal_states+=1
            ordering.append(
                i)  # we now know in which order should the matrix be transformed for applyinh limiting markovv matrix
            l[i][i] = 1
            sumofrow[i]=1
            # f(1,1) so that we can easily check later whether a state is terminal or not
    for i in range(len(terminalstate)):
        # since all the terminal states have been added all non terminal states can now be added
        if terminalstate[i] == False:
            number_of_non_terminal_states+=1
            ordering.append(i)
    # print("Ordering",ordering)
    # now that we know how the matrix has to be reordered we can easily reorder it
    reordered_l = [[f(0, 1) for j in range(len(l[0]))] for i in range(len(l[0]))]
    for i in range(len(l[0])):
        for j in range(len(l[0])):
            reordered_l[i][j] = f(l[ordering[i]][ordering[j]],sumofrow[ordering[i]])
    # return 0 # breakpoint
    # recur = [0 for temp4 in range(len(l[0]))]
    # realprob = [0 for temp5 in range(len(l[0]))]
    ansprob = [0 for temp6 in range(len(l[0]))]

    # to get the limiting matrix we need to separte out a sub matrix of non terminal states
    # They can be sliced by sa follows: reordered_l[-2:][:number_of_terminal_states]
    B=[temp[0:number_of_terminal_states] for temp in reordered_l[-number_of_non_terminal_states:]]
    #A*B is the answer we are looking for
    #where A=[I-Q]^-1
    #print(reordered_l)
    Q=[temp[number_of_terminal_states:] for temp in reordered_l[-number_of_non_terminal_states:]]
    #print(Q)
    #print("*")
    #Doing I-Q
    for i in range(len(Q)):
        for j in range(len(Q)):
            if i!=j:
                Q[i][j]=f(0,1)-Q[i][j]
            else:
                Q[i][j]=f(1,1)-Q[i][j]
    #print(Q)
    #taking inverse
    A=inversecalc(Q)
    #print(A)
    ansprob=matmul(A,B)[0]
    #print(AB)
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    def lcm(a, b):
        return (a * b) / gcd(a, b)

    '''def util(start, visited, probability, recur, realprob):
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
        # print(probability, start)
        # print(recur, realprob)
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
        util(0, visited, probability, recur, realprob)  # main cauclation starter
        visited = [False for i in range(len(l[0]))]
        for i in range(len(l[0])):
            visited = [False for j in range(len(l[0]))]
            dfs2(i, i, visited)

    dfs()
    # print(connected)
    # print("#######################")
    # print(realprob)
    # calculation of the final probabilities are done below
    for i in range(0, len(l[0])):
        if recur[i] != 0:
            for j in connected[i]:
                ansprob[j] += (realprob[j] * recur[i] / (
                        1 - recur[i]))  # edited this line and added the below line press ctrl+z tomorrow
        ansprob[i] += realprob[i]
    '''
    maxdenominator = 1
    # print(ansprob)
    # ansprob.append(f(1,10))
    # this just gets the max denominator but remmeber to take gcd tomorrow to get the correct ans in case of(1/3,7/22)type of fractions and get 66 as the common denominator
    for i in range(0, len(ansprob)):
        maxdenominator = int(lcm(ansprob[i].denominator, maxdenominator))
    #print(maxdenominator)
    #print(ansprob)
    final_numerator=[]
    for i in range(0, len(ansprob)):
        if ansprob[i].denominator != maxdenominator:
            tobemultipliedby = int(maxdenominator / ansprob[i].denominator)
            final_numerator.append(ansprob[i].numerator*tobemultipliedby)
            #ansprob[i] *= (f(tobedividedby, 1))
        else:
            final_numerator.append(ansprob[i].numerator)
    final_numerator.append(maxdenominator)
    return final_numerator
print(solve(l))
#print(inversecalc(toinverse))
#print(inversecalc(toinverse))
