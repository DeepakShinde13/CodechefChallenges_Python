# cook your code here
t = input()
for _ in range(t):
    n = input()
    a = raw_input()
    b = raw_input()
    up = 0
    down = 0 
    count = 0
    
    if a.count('*')>0:
        up = 1
    if b.count('*')>0:
        down = 1
    if up==1 and down ==1 :
        count +=1
        
    ustack = []
    dstack = []
    
    for i in range(n):
        if a[i] == "*":
            if len(ustack)==0:
                ustack.append("*")
            else:
                if ustack[-1]=="#":
                    ustack.append("*")
                elif ustack[-1]=="*":
                    ustack.append("#")
                    dstack.append("#")
                    ustack.append("*")
        if b[i] == "*":
            if len(dstack)==0:
                dstack.append("*")
            else:
                if dstack[-1]=="#":
                    dstack.append("*")
                elif dstack[-1]=="*":
                    ustack.append("#")
                    dstack.append("#")
                    dstack.append("*")
                    
    count += ustack.count("#")
    print count, ustack,dstack
        
            
        
                
    print count