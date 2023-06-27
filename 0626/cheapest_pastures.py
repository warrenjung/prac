big=int(10e9)
n,m=input().split()
n,m=int(n),int(m)
edges=[]
for jnk in range(m):
    a,b,c=input().split()
    a,b,c=int(a)-1,int(b)-1,int(c)
    edges.append([a,b,c])
dist=[big]*n
dist[0]=0
flag=True
for cycle in range(n-1):
    flag=True
    for curedge in edges:
        if dist[curedge[1]]>dist[curedge[0]]+curedge[2]:
            flag=False
            dist[curedge[1]]=dist[curedge[0]]+curedge[2]
    if flag:
        break
flag=True
for curedge in edges:
    if dist[curedge[1]]>dist[curedge[0]]+curedge[2]:
        flag=False
        dist[curedge[1]]=dist[curedge[0]]+curedge[2]
if flag:
    for ans in dist:
        print(ans)
else:
    print('moo')
