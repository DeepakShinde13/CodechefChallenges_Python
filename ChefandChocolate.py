__author__ = 'Deepak'
t=input()
while(t>0):
    t-=1
    n,m= map(int,raw_input().split())
    if n==1 and m==1:
        print "No"
    elif n==1:
        if m%2!=0: print "No"
        else:print "Yes"
    elif m==1:
        if n%2!=0 : print "No"
        else: print "Yes"
    else:
        if n%2==0 and m%2==0:print "Yes"
        if n%2!=0 and m%2!=0:print "No"
        if n%2==0 and m%2!=0: print "Yes"
        if n%2!=0 and m%2==0: print "Yes"