__author__ = 'Deepak'
t=input()
for _ in range(t):
    n= input()
    a=map(int,raw_input().split())
    if sum(a)==n: print n
    else: print n-(sum(a)%n)