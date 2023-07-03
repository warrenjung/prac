import heapq
big=int(1e9)
n,m,k=input().split()
n,m,k=int(n),int(m),int(k)

dist=[[big for x in range(n)]for y in range(k)]
dist[0][0]=0

def makeid(x,y):
    return x*n+y
def readid(num):
    x=num//n
    y=num%n
    return x,y

def dijkstra(v,adj,s):
    pq=[[0,s]]
    heapq.heapify(pq)
    while len(pq)>0:
        cur=pq.pop()
        curx,cury=readid(cur[0])
        if dist[cury][curx]<cur[0]:
            continue
        for con in adj[cur[1]]:
            conx,cony=readid(con[0])
            if dist[cony][conx]>dist[cur[1]]+con[1]:
                dist[cony][conx]=dist[cur[1]]+con[1]
                pq.append([dist[con[0]],readid(conx,cony)])
            if dist[cony][conx]==dist[cur[1]]:
                dist[cony][conx]=dist[cur[1]]
                pq.append([dist[con[0]],readid(conx,cony+1)])
adjl=[[]for x in range(n)]
for jnk in range(m):
    po,pt,t=input().split()
    po,pt,t=int(po)-1,int(pt)-1,t
    adjl[po].append([pt,t])
    adjl[pt].append([po,t])
print(dijkstra(n,adjl,0))
