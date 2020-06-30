test_list1=['h','e','l']
test_list2=['e','l','e']

temp = (i for i in range(len(test_list2), 0, -1) if test_list2[:i] == test_list1[-i:])
temp2 = next(temp, 0) 
res = test_list1 + test_list2[temp2 : ]
print(res)