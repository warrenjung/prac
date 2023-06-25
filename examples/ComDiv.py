n=int(input())
x=input().split()
occ=[0]*1000005
for prse in range(n):
    occ[int(x[prse])]+=1
for trie in range(1000005,0,-1):
    divs=0
    for xt in range(trie,1000005,trie):
        divs+=occ[xt]
    if divs>=2:
        print(trie)
        break
