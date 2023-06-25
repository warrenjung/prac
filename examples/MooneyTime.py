#initialization
n,m,c=int(input())
n=int(n)
m=int(m)
c=int(c)
valist=input().split()
for prse in range(n):
    valist[prse]=int(valist[prse])
paths=[[]for x in range(n)]
for prse in range(m):
    strt,end=input().split()
    strt=int(strt)
    end=int(end)
    paths[strt-1].append(end-1)
poslist=[["N/A" for prse in range(1000)]for prse in range(n)]
stck=[[0,0,valist[0]]]
#where,when,what
while True:
    if len(stck)==0:
        break
    val=stck.pop(0)
    if stck[1]>1000:
            break
    for dest in paths[val[0]]:
        if poslist[dest][val[1]+1]=="N/A":
            if val[2]+valist[dest]-(c*(val[1]+1)**2)<0:
                continue
            poslist[dest][val[1]+1]==val[2]+valist[dest]-(c*(val[1]+1)**2)
            stck.append([dest,val[1]+1,val[2]+valist[dest]-(c*(val[1]+1)**2)])
        else:
            if val[2]+valist[dest]-(c*(val[1]+1)**2)>poslist[dest][val[1]+1]:
               poslist[dest][val[1]+1]==val[2]+valist[dest]-(c*(val[1]+1)**2)
               stck.append([dest,val[1]+1,val[2]+valist[dest]-(c*(val[1]+1)**2)]) 
print(valist)
