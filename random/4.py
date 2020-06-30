

def maxSubArraySum(a, size):
    max_so_far = -9999999999
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far <= max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    print(max_so_far-max(a[start:end+1]))


nn=int(input())
arr=list(map(int,input().split()))
maxSubArraySum(arr,nn)