def solution(total_lambs):
    total_lambs=int(total_lambs)
    #Since we arent sure whether we are being passed a string or an int
    being_stringent = 0
    # we checck 1 2 4 8 16 .... in reverse order
    for i in range(32, 0, -1):
        if (2 ** i) - 1 <= total_lambs:
            being_stringent = i
            break
    if total_lambs - (2 ** being_stringent) - 1 >= (2 ** (being_stringent - 1)):
        being_stringent += 1  # for the case where the last member can be repeated like 1,2,4,4 for x between 11 and 15
    # like nth fibonacci number due to the condition that the next two subordinates sum cant be more than the current
    prev2 = 0
    prev = 1
    curr = 1
    summ=1
    being_generous = 1
    for i in range(100):
        curr = prev + prev2
        prev2 = prev
        prev = curr
        summ+=curr
        if summ > total_lambs:
            break
        being_generous += 1
    print(being_generous - being_stringent)
solution(10)