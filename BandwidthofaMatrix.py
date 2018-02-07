__author__ = 'Deepak'
t = input()
for _ in range(t):
    n = input()
    arr = []
    zeros = 0
    ones = 0
    for i in range(n):
        row = map(int,raw_input().split())
        arr.append(row)
        for j in range(len(row)):
            if row[j] == 0:
                zeros +=1
            else:
                ones += 1
    #print arr
    #print zeros, ones
    #bandwidth = 0
    temp = n
    i =1
    while(True and i<=n):
        if ones<=temp :
            print i-1
            break
        else:
            temp = temp +(n-i)*2
            i+=1


