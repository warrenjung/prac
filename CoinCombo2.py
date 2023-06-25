coins,sum=input().split()
coins=int(coins)
sum=int(sum)
coinlist=input().split()
dplist=[0]*(sum+1)
dplist[0]=1
for ind in range(coins):
    coinlist[ind]=int(coinlist[ind])
for coin in coinlist:
    for ind in range(sum+1):
        if ind-coin>0:
            dplist[ind]+=dplist[ind-coin]

print(dplist[sum])