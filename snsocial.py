from collections import defaultdict

t = input()

def DFS(node):

    #print alist, "HI"
    visited[node] =1
    #print alist[node], "ALIST"
    for j in (alist[node]):
        if (visited[j] == 0):
            DFS(j)



for __ in range(t):
    n, m = map(int,raw_input().split())



    count = 0
    visited = [0]*n

    alist = defaultdict(list)

    for _ in range(m):
        x,y = map(int,raw_input().split())
        alist[x-1].append(y-1)
        alist[y-1].append(x-1)
    for i in range(n):
        if visited[i]==0 :
            DFS(i)
            count+=1

    print count, alist, "ALIST"
    d = []
    for i in range(n):
        temp = 0
        for j in range(len(alist)):
            if len(alist[j])<=i:
                temp+=1
        #print temp,"TEMP"
        if temp==n:
            d.append(temp-1)
        else:
            d.append(count+temp-1)
    #print d,"D"
    for i in d:
        print i,