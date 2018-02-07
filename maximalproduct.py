mod = 1000000000+7
 
def count_neg(a):
    ans = 0
    for i in a:
        if i < 0:
            ans += 1
    return ans
 
def prod(a):
    ans = 1
    for i in a:
        ans = (ans*i)%mod
    return ans
 
for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    if k == n:
        print(prod(a))
        
    else:
        b = sorted(a, key=abs)
        negs = count_neg(b[n-k:])
        if negs %2 == 0:
            print(prod(b[n-k:]))
        else:
            flag1 = False
            flag2 = False
            
            i1 = n-k-1
            while(i1 >= 0):
                if b[i1] >0:
                    break
                i1-=1
            j1 = n-k
            while(j1<n):
                if b[j1] < 0:
                    break
                j1+=1
            if i1 != -1:
                rat1 = abs(b[i1]/b[j1])
            else:
                flag1 = True
            i = n-k-1
            j = n-k
            while i>=0:
                if b[i] < 0:
                    break
                i-=1
            while j <n:
                if b[j] > 0:
                    break
                j+=1
            if i !=-1 and j != n:
                rat2 = abs(b[i]/b[j])
            else:
                flag2 = True
            if not flag1 and not flag2:
                if rat1 > rat2:
                    b[i1], b[j1] = b[j1], b[i1]
                else:
                    b[i], b[j] = b[j], b[i]
            else:
                if flag1 and flag2:
                    print(prod(b[:k]))
                    continue
                elif flag1:
                    b[i], b[j] = b[j], b[i]
                else:
                    b[i1], b[j1] = b[j1], b[i1]
            print(prod(b[n-k:])) 