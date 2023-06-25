

import math
def factorial(n):
    x=[1]*(n+1)
    total=1
    for xz in range(2,n+1):
        x[xz]=(total)*xz
        total=x[xz]
    return x
wrd=input()
factl=[1]*(len(wrd)+1)
alpha=[0]*26
tot=1
m=(10**9)+7
mx=len(wrd)
for prse in range(len(wrd)):
    alpha[ord(wrd[prse])-97]+=1
    tot=tot*(prse+1)%m
    factl[prse+1]=tot
for x in range(26):
    #print(pow(factl[alpha[x]],m-2,m)%m)
    tot=tot*pow(factl[alpha[x]],m-2,m)%m
print(int(tot))