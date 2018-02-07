import math
def primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False
 
    return [2]+[i for i in range(3,n,2) if sieve[i]]
    #return sieve
 
        
def f(l,r,x,y):
    result = 0
    for i in range(x,y+1):
        if dd[i]:
            for j in range(l-1, r):
                number = a[j]
                ex = 0 
                while(number%i==0):
                    ex+=1
                    number = number/i
                result+=ex
                    
    return result
 
n = input()
a = map(int, raw_input().split())
q = input()
d = primes(1000000+1)
dd = [False]*(1000000)
for i in d:
    dd[i] = True
#print d
for _ in range(q):
    l,r,x,y = map(int, raw_input().split())
    #d = primes(y+1)
    print f(l,r,x,y)