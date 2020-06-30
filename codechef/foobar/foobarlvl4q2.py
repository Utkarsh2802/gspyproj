def solution(entrances, exits, path):
    ans = 0                                                                     #Since there is no cycle i.e after exiting a room u cant get in the same room we can just summ of the net outflows from each of the intermediate rooms to get the ans
    outflow_intermediate_path=[]
    for i in range(len(path) - len(entrances) - len(exits)):
        outflow_intermediate_path.append(sum(path[len(entrances)+i]))             # to store the total outflows from each path i.e  max number of bunnies who can exit the intermediate path
    for i in range(len(path) - len(entrances) - len(exits)):                 # for each of the intermediate room
        max_inflow_of_bunnies = 0                                                        # Sum of bunnies that enter that room
        for j in entrances:
            max_inflow_of_bunnies += path[j][len(entrances) + i]                         #max_inflow= total number of bunnies that other can send to this particular intermediate room
        ans += min(max_inflow_of_bunnies, outflow_intermediate_path[i])        #if 9 bunnies enter in a room with capacity 8 then only 8 can go out else if  less than 8 enter they all can go out thus we can usa a min function here
    return ans
