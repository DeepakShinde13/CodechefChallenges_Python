__author__ = 'Deepak'
from collections import defaultdict

def pal(dum):
    t = len(dum)


    L = [[0 for x in range(t)] for x in range(t)]

    for i in range(t):
        L[i][i] = 1


    for cl in range(2, t+1):
         for i in range(t-cl+1):
             j = i+cl-1
             if dum[i] == dum[j] and cl == 2:
                 L[i][j] = 2
             elif dum[i] == dum[j]:
                 L[i][j] = L[i+1][j-1] + 2
             else:
                 L[i][j] = max(L[i][j-1], L[i+1][j])
         # for i in L:
         #     print i
         # print cl

    return L[0][t-1]


def dfs(i):
    visited[i]= True
    bum[i] = counter
    for i in alist[i]:
        if not visited[i]:
            dfs(i)



alist = defaultdict(list)
n, k, m = map(int, raw_input().split())
for _ in range(k):
    x, y  = map(int, raw_input().split())
    alist[x-1].append(y-1)
    alist[y-1].append(x-1)
num = map(int, raw_input().split())
bum = {}
dum = []

counter = 0
visited = [False]*n

for i in range(n):
    if not visited[i]:
        dfs(i)
        counter +=1
#print counter,alist
for i in num:
    dum.append(bum[i-1])

print pal(dum)