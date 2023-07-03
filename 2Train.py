import heapq
big=int(1e20)
a,b,n=input().split()
a,b,n=int(a)-1,int(b)-1,int(n)
adjl=[[]for x in range(1000)]
pq=[[0,0,a,-1]]
#cost,trains_used,cur,prev
heapq.heapify(pq)
dist=[[big,big]]*1000
dist[a]=[0,0]
#cost,trains_used
def dijkstra(v,adj,s):
    while len(pq)>0:
        cur=pq.pop()
        if dist[cur[2]][0]<cur[0]:
            continue
        for con in adj[cur[2]]:
            if cur[3]==con[2]:
                if dist[con[0]][0]>dist[cur[2]][0]:
                    #print(cur)
                    #print(con)
                    dist[con[0]]=[dist[cur[2]][0],cur[1]+1]
                    pq.append([dist[con[0]][0],cur[1]+1,con[0],con[2]])
                    #print(dist)
                if dist[con[0]]==dist[cur[2]][0]:
                    if dist[con[0]][1]>cur[1]+1:
                        dist[con[0]][1]=cur[1]+1
                        pq.append([dist[con[0]][0],cur[1]+1,con[0],con[2]])
                continue
            if dist[con[0]][0]>dist[cur[2]][0]+con[1]:
                #print(cur)
                #print(con)
                dist[con[0]]=[dist[cur[2]][0]+con[1],cur[1]+1]
                pq.append([dist[con[0]][0],cur[1]+1,con[0],con[2]])
                #print(dist)
            if dist[con[0]]==dist[cur[2]][0]+con[1]:
                if dist[con[0]][1]>cur[1]+1:
                    dist[con[0]][1]=cur[1]+1
                    pq.append([dist[con[0]][0],cur[1]+1,con[0],con[2]])
    return dist

    

for jnk in range(n):
    cost,routes=input().split()
    cost,routes=int(cost),int(routes)
    trout=input().split()
    prev=int(trout[0])-1
    for ind in range(1,routes):
        adjl[prev].append([int(trout[ind])-1,cost,jnk])
        prev=int(trout[ind])-1
l=dijkstra(1000,adjl,a)
#print(l)
l=l[b]
if l[0]==big:
    print(-1,-1)
else:
    print(l[0],l[1])