__author__ = 'Deepak'
from fractions import gcd
t=input()
while(t>0):
    t-=1
    n,c = map(int,raw_input().split())
    temp= n*(n+1)/2
    #print temp, "temp"
    if n==1:
        print "Yes"
    elif n==2 and c>=temp:
        print "Yes"

    elif gcd(c,n)>1 and c >= temp :
        print "Yes"
    else:
        print "No"