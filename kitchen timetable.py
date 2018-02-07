__author__ = 'Deepak'
t=input()
while(t>0):
    t-=1
    n=input()
    a=map(int,raw_input().split())
    b=map(int,raw_input().split())
    count=0
    m=0
    for i in range(len(a)):
        if m+b[i]<=a[i]:
            count+=1
        m=a[i]
    print count