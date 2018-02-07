__author__ = 'Deepak'

from collections import defaultdict
for _ in range(input()):
    n, d = map(int, raw_input().split())
    arr = {}
    totallec = 0
    totalsad = 0
    for __ in range(n):
        di,ti,si = map(int, raw_input().split())
        if si not in arr:
            arr[si] = ti
            totallec += ti
            totalsad += si*ti
        else:
            arr[si] += ti
            totallec += ti
            totalsad += si*ti

    # for k in arr:
    #     print arr[k] , k
    # print "////"
    #print totalsad, "sad"
    if totallec <= d:
        print 0
    else:
        #k = sadness
        #v = days
        for k, v in sorted(arr.items(), reverse=True):
            #print k, v
            if d-v > 0:
                d -= v
                totalsad -= v*k
            elif d-v == 0:
                totalsad -= v*k
                print totalsad
                break
            elif d-v < 0:
                totalsad -= d*k
                print totalsad
                break