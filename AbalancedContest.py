__author__ = 'Deepak'
t = input()
for _ in range(t):
    n, p = map(int, raw_input().split())
    x1 = 0
    x2 = 0
    a = map(int, raw_input().split())
    for i in range(len(a)):
        if a[i]>= int(p/2):
            x1+=1
        elif a[i]<= int(p/10):
            x2+=1

    #print x1,x2
    if x1==1 and x2==2:
        print "yes"
    else:
        print "no"