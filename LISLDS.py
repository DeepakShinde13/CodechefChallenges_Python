__author__ = 'Deepak'
t=input()
while(t>0):
    t-=1
    n,a,b = map(int,raw_input().split())
    if a+b-1>n:
        print "-1"
    else:
        x=1
        y=