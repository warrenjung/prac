coins,sum=input().split()
coins=int(coins)
sum=int(sum)
coinlist=input().split()
dplist=[0]*(sum+1)
dplist[0]=1
for ind in range(coins):
    coinlist[ind]=int(coinlist[ind])
for ind in range(sum):
    for m in coinlist:
        if ind+m>sum:
            break
        dplist[ind+m]+=dplist[ind]

print(dplist[sum])