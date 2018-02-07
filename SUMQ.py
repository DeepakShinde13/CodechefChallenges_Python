for _ in range(input()):
    p,q,r = map(int,raw_input().split())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    c = map(int, raw_input().split())

    a.sort(reverse = True)
    c.sort(reverse = True)
    b.sort(reverse = True)

    s = 0
    s1 = sum(a)
    s2 = sum(c)
    j = 0
    k = 0
    temp1= 0
    temp2=0
    for i in range(len(b)):
        t1 = 0
        t2 = 0
        ss1 = 0
        ss2 = 0

        while(j<len(a) and a[j]>b[i] ):
            temp1+=a[j]
            j+=1

        while(k<len(c) and c[k]>b[i] ):
            temp2+=c[k]
            k+=1

        ss1 = s1-temp1
        ss2 = s2-temp2

        #break as there is no use to progress

        if ss1 == 0 or ss2==0:
            break
        t1 = len(a)-j
        t2 = len(c)-k

        s += ((t1*b[i]+ ss1)*(t2*b[i]+ss2))%1000000007

    print s%1000000007