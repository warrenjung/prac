fin=open("cbarn2.in","r")
fout=open("cbarn2.out","w")
doors,open=fin.readline().split()
doors=int(doors)
open=int(open)
doordem=[]
for prse in range(doors):
    amount=int(fin.readline())
    doordem.append(amount)
mindist=9999999999999999999999999999
dp=[[99999999999999999999999999999 for prse in range(doors+1)]for prse in range(open+1)]
#DP[doors opened][pos]
for prse in range(doors):
    dp=[[99999999999999999999999999999 for prse in range(doors+1)]for prse in range(open+1)]
    dp[0][doors]=0
    for du in range(1,open+1):
        for fp in range(doors):
            partdist=0
            for sp in range(fp+1,doors+1):
                partdist+=(sp-fp-1)*doordem[sp-1]
                newdist=dp[du-1][sp]
                if newdist<9999999999999999999999999999:
                    newdist+=partdist
                dp[int(du)][int(fp)]=min(dp[int(du)][int(fp)],newdist)
    mindist=min(mindist,dp[open][0])
    x=doordem.pop(0)
    doordem.append(x)
fout.write(str(mindist))