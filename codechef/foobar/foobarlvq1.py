from itertools import combinations

def answerr(num_buns, num_required):
    bun = [[i] for i in range(num_buns)]
    buns = [[] for i in range(num_buns)]

    if num_required == 0:
        return buns
    start = 0
    print(list(combinations(bun, num_buns - num_required + 1)))
    for c in combinations(buns, num_buns - num_required + 1):
        for item in c:
            item.append(start)
            print(buns)
        print("-----")
        start += 1
    return buns
from itertools import combinations
def solution(num_buns, num_required):
    #For all combintions of size num_required-1 from num_buns there should be atleast one unique key missing
    #Each key should be repeated exactly (num_buns-num_required)+1
    #Ex: suppose 10 bunnies are required to open the cell and there are 100 bunnies if key 'x' is repeated less than 90 times then we can choose 10 bunnies such that key 'x' is not among
    #thus we need each key to be repeated 91 times in the abpve example
    answer=[[] for i in range(num_buns)]
    initial_key = 0
    for i in combinations(answer,num_buns-num_required+1):
        for j in i:
            j.append(initial_key)
        initial_key+=1
    return answer
print(solution(5,3))