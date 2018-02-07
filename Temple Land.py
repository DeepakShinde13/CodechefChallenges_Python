__author__ = 'Deepak'
s = input()
for _ in range(s):
    n = input()
    a = map(int, raw_input().split())
    if (a[0] == 1 and a[-1] == 1 and len(a)%2!=0 and a[int(len(a)/2)]==max(a)):
        f=0
        for i in range(len(a)-1):
            if (abs(a[i]-a[i+1])!=1):
                print "no"
                f=1
                break
        if f==0:
            print "yes"

    else:
        print "no"