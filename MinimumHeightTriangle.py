import math
a = input()
s = 2
while(True):
    if int(math.sqrt(a*a+s*s))==math.sqrt(a*a+s*s):
        print a, s, int(math.sqrt(a*a+s*s))
        break
    else:
        s+=1