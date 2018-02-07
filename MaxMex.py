__author__ = 'Deepak'
for _ in range(input()):
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()
    c = 0
    z = 0
    flag = 0
    if a[0] != 0:
        if k==0:
            print 0
            continue

        c+= a[0]
        if c>k and k!=0:
            print k
            continue

    for i in range(1, len(a)):
        #print a[i], "HI"
        #print c,"HIINSIN"
        temp = a[i]-a[i-1]-1
        if temp >= 1:
            if c+temp <= k:
                c += temp
            elif c+temp>k:
                z = a[i-1]+k-c+1
                flag = 1
                break
    #print c, "C"
    if flag == 0:
        print a[-1]+k-c+1
    else:
        print z
