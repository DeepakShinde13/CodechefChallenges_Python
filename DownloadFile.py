__author__ = 'Deepak'
t1 = input()
while(t1>0):
    t1-=1
    n, k = map(int, raw_input().split())
    money = 0
    for i in range(n):
        t, d = map(int,raw_input().split())
        if(k-t >=0 and k!=0):
            k -= t
            continue
        elif k==0:
            money += d*t
        else:
            money += (t-k)*d
            k = 0
    print money

