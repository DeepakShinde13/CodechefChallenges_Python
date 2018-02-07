__author__ = 'Deepak'
t=input()
while(t>0):
    t-=1
    n=input()
    b=map(int,raw_input().split())
    f= False
    fl = False
    for i in b:
        if i == 5:
            fl= True
        if i<=2:
            f=True
            break
    if f:
        print "No"

    elif sum(b)/float(n) >=4.0 and fl:
        #print sum(b)/float(n)
        print "Yes"
    else:
        #print sum(b)/float(n)
        print "No"