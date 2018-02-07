t = input()
def find(a,b):
    flag = 0
    count = 0
    f1 = "##"
    f2 = "#."
    f3 = ".#"
    f4 = ".."
    hashcount = 0
    set1 = False
    set2 = False
    if len(a)==1 and a[0]=="." and b[0]==".":
        return False

    for i in range(len(a)-1):
        temp = a[i]+b[i]
        temp2= a[i+1]+b[i+1]

        if count ==2 and (temp!=f4):
            flag =1
            break
        if temp == f2 and temp2==f3:
            flag =1
            break
        if temp == f3 and temp2==f2:
            flag =1
            break
        if temp == f1 :
            count = 1
            if(set1==True or set2==True):
                hashcount +=1

        if temp == f2 :
            count = 1
            if set1==True and hashcount%2!=0:
                flag =1
                break
            elif set2==True and hashcount%2==0:
                flag =1
                break
            else:
                set1=True
                set2=False
                hashcount = 0
                continue
        if temp == f3:
            count = 1
            if set2==True and hashcount%2!=0:
                flag =1
                break
            elif set1==True and hashcount%2==0:
                flag =1
                break
            else:
                set2=True
                set1=False
                hashcount = 0
                continue

        if temp==f4 and count == 1 :
            count = 2

    if len(a)>1:
        if count ==2:
            if a[-1] == "#" or b[-1]=="#":
                flag =1
        te = a[-1]+b[-1]
        if te == f2 :
            if set1==True and hashcount%2!=0:
                flag =1
            elif set2==True and hashcount%2==0:
                flag =1
        if te == f3 :
            if set2==True and hashcount%2!=0:
                flag =1
            elif set1==True and hashcount%2==0:
                flag =1

    if flag ==1:
        return False
    else:
        return True




for _ in range(t):
    n = input()
    a = raw_input()
    b = raw_input()
    if find(a,b):
        print "yes"
    else:
        print "no"