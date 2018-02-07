__author__ = 'Deepak'

def lex_min(z):
    #print "z",z
    mini = 20000
    el=""
    for i in range(len(z)):
        if ord(z[i])<mini:
            mini =ord(z[i])
            el = z[i]
    #storing each such smallest string
    indices=[pos for pos, char in enumerate(z) if char == el]
    #print indices,'incixf'
    str=[]
    #print index
    for i in indices:
        str.append(''.join(z[i:]+z[:i]))
    #print str,'str'
    #print min(str),'minstr'
    return min(str)


s = list(raw_input())
q = input()
while(q>0):
    q-=1
    a=raw_input().split() #input of query
    if len(a)==3:
        c=int(a[1])
        s[c-1]=a[2]
        #print s
    else:
        z=s[int(a[1])-1:int(a[2])]
        #print ''.join(z)
        substring = lex_min(z)
        print substring[int(a[3])-1]