coins,sum=input().split()
coins=int(coins)
sum=int(sum)
coinlist=input().split()
dplist=['n/a']*(sum+1)
dplist[0]=0
for ind in range(coins):
    coinlist[ind]=int(coinlist[ind])
for ind in range(sum):
    for m in coinlist:
        print(dplist)
        if ind+m>sum:
            continue
        if dplist[ind+m]=='n/a' or dplist[ind+m]>dplist[ind]+1:
            dplist[ind+m]=dplist[ind]+1
print(dplist[sum])