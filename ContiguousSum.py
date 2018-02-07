__author__ = 'Deepak'
t= input()
#typical Kadane's algorithm
def maxContiguousSum(a):
    flag = 0
    for i in range(len(a)):
        if a[i]>0:
            flag=1
            break
    if(flag==0):
        return max(a)

    global_max = 0
    last_max = 0

    for i in range(len(a)):
        last_max += a[i]
        if last_max < 0:
            last_max = 0

        elif (global_max < last_max):
            global_max = last_max

    return global_max

if t>=3:
    a = map(int, raw_input().split())
    print maxContiguousSum(a)

