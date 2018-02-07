__author__ = 'Deepak'
t=input()
while(t>0):
    t-=1
    n=input()
    s=map(int,raw_input().split())
    d=map(int,raw_input().split())
    com=len([x for x in s if x in d])
    j=n-com #different elements
    if j==0:
        print "1"
        for i in range(n):
            print (i+1)%n+1,
        print
    elif j==1:
        print "0"
        for i in range(n):
            print (i+1)%n+1,
        print
    elif j==n:
        print "0"
        for i in range(n):
            print i+1