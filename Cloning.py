__author__ = 'Deepak'
t = input()
for _ in range(t):
    n, q = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    for __ in range(q):
        a,b,c,d = map(int, raw_input().split())
        t1 = sorted(arr[a-1:b])
        t2 = sorted(arr[c-1:d])
        count = 0
        f = 0
        for i in range(len(t1)):
            if(t1[i]!=t2[i]):
                count+=1
                if count >= 2:
                    print "NO"
                    f=1
                    break
        if f==0:
            print "YES"