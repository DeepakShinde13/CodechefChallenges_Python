__author__ = 'Deepak'
t = input()
for __ in range(t):
    n = input()
    a = map(int, raw_input().split())
    a.sort(reverse=True)
    s = -9999999999
    temp = 0
    tot = 0
    c = -1
    #print a
    for i in range(len(a)):
        if ((tot+a[i])*(i+1))>= s:
            tot += a[i]
            s = (tot)*(i+1)
            #print s, tot, "TOT"
        else:
            c = i
            break

    if c==-1:
        print s
    else:
        print s+sum(a[c:])

