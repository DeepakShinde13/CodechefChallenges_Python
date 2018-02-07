def dp(a):
    
    if flag : 
        return max(a)
        
    mat = [[0 for j in range(len(a))]for i in range(len(a))]
    #print mat
    maxi = 0
    
    for i in range(len(a)):
        mat[i][i] = a[i]
        if mat[i][i]>maxi:
            maxi = mat[i][i]
    
        
    
    for c in range(2, len(a)+1):
        for i in range(len(a)+1-c):
            j = c+i-1
            
            if i+1== j and c==2:
                mat[i][j] = a[i]+a[j]
            else:
                mat[i][j] = a[i]+ mat[i+1][j]
                
            if mat[i][j] > maxi:
                maxi = mat[i][j]
                
        # for k in mat:
        #     print k
        # print '//////////////'
    
    return maxi
    
def isneg(a):
    neg = 0
    for i in a:
        if i < 0:
            neg+=1
    if neg == len(a):
        return True
    else:
        return False

def nconti(a):
    s = 0
    maxi = 0
    if flag:
        return max(a)
    else:
        
        for i in a:
            if i>=0:
                s+=i
        return s

flag = False
for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    flag = isneg(a)
    print  dp(a), nconti(a)