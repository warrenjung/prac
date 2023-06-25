fin=open("help.in","r")
fout=open("help.out","w")
n=int(fin.readline())
m=(10**9)+7
nl=[]
for prse in range(n):
    s,e=fin.readline().split()
    s=int(s)
    e=int(e)
    nl.append([s,1])
    nl.append([e,-1])
nl.sort()
d=[-1]*(n+1)
tot=1
for prse in range(n+1):
    d[prse]=tot
    tot=(tot*2)%m
print(d)
ans=0
prefsum=0
for gs in nl:
    prefsum+=gs[1]
    if gs[1]==1:
        print(n-prefsum)
        ans=(ans+d[n-prefsum])%m
fout.write(str(ans))