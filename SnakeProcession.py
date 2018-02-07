t = input()

for _ in range(t):
    l = input()
    s = raw_input()
    m = []
    for i in range(len(s)):
        if s[i]!=".":
            m.append(s[i])
    #print m
    if len(m)%2!=0:
        print "Invalid"
    else:
        flag = 0
        for i in range(len(m)):
            if(i%2==0 and m[i]!="H"):
                flag = 1
                break
            elif(i%2!=0 and m[i]!="T"):
                flag = 1
                break
        if flag == 0:
            print "Valid"
        else:
            print "Invalid"