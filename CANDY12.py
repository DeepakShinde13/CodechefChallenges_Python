def find(a,k):
    if k==len(a):
        return a.count(1)
    count= 0
    b = []
    temp = 0
    while(temp<len(a)):
        b.append(a[:k].count(1))
        a = a[-1:]+a[:-1]
        temp+=1
    return b

n, k, p = map(int, raw_input().split())
a = map(int, raw_input().split())
s = raw_input()
if k > n:
    k = n

b = find(a,k)
#print "B", b
x=0
for i in range(len(s)):

    if s[i]=='?':
        if n==k:
            print a.count(1)
            continue
        #print x
        # z = b[x-n+k:]
        # zz = b[:x+1]
        # print z, zz
        if x-n+k<0:
            print max(max(b[x-n+k:]), max(b[:x+1]))
        else:
            print max(b[x-n+k:x+1])
    elif (s[i] =='!'):
        x= (x+1)%n

