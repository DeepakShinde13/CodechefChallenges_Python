__author__ = 'Deepak'
def findbin(arr, k):
    te = 0
    m = len(arr)
    for i in range(m):
        te+= 2**(k-arr[i])
    #print te
    return te
for _ in range(input()):
    n,k = map(int, raw_input().split())
    temp = []
    d = []
    for i in range(n):
        temp = map(int, raw_input().split())
        #d.append()
        d.append(findbin(temp[1:],k))
    ke = ['1']*k
    bink = int(''.join(ke),2)

    #print bink, d
    count = 0
    for j in range(len(d)-1):
        if d[j] == bink:
            count+=len(d)-j-1
        else:
            for k in range(j+1, len(d)):
                if d[j] | d[k] == bink:
                    count+=1
    print count
