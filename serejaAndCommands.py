__author__ = 'Deepak'
t = input()
for _ in range(t):
    n, m = map(int, raw_input().split())
    d = []
    vec = [1]*n
    for __ in  range(m):
        a,b,c = map(int,raw_input().split())
        d.append([a,b,c])
    d = d[::-1]
    for temp in range(len(d)):
        a,b,c = d[temp][0],d[temp][1],d[temp][2]
        if a==2:
            for i in range(b-1, c):
                vec[i]+=



