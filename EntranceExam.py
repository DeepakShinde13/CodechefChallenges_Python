__author__ = 'Deepak'
t=input()
for _ in range(t):
    d=[]
    n,k,e,m = map(int,raw_input().split())
    for i in range(n-1):
        line= map(int,raw_input().split())
        d.append(sum(line))
    my = sum(map(int,raw_input().split()))
    #print my, "My"
    #d.append(my)
    d.sort(reverse=True)
    #print d
    score= d[k-1]+1-my
    if score>m:
        print "Impossible"
    elif score<0:
        print "0"
    else:
        print score
