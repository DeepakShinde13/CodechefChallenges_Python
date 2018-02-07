__author__ = 'Deepak'
t=input()
while t>0:
    t-=1
    n=input()
    b=raw_input()
    x=map(int,raw_input().split())
    c=[]
    for i in range(len(b)):
        c.append(int(b[i]))
    cost=0
    m1=0
    m2=0
    #print c
    #print x
    temp=[]
    x1=0
    x2=0
    sub=0
    for i in range(n-1):

        if c[i]==1 and m1==0:
            m1=1
            x1=x[i]
        if c[i]==0 and m1==1:
            temp.append(x[i])
            sub+= x[i+1]-x[i]
            cost+=x[i+1]-x[i]
        if c[i]==0 and m1==0:
            cost+=x[i+1]-x[i]
        if c[i] == 1 and m1==1:
            x2=x[i]
            for i in range(len(temp)):
                if abs(temp[i]-x1)<abs(temp[i]-x2) and x1!=0 and x2!=0:
                    cost+=abs(temp[i]-temp[i-1])
                else:
                    cost+=abs(temp[i+1]-temp[i])

            cost-=sub


 
    print cost