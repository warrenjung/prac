fin=open('teamwork.in','r')
fout=open('teamwork.out','w')
numcows,groupsize=fin.readline().split()
numcows,groupsize=int(numcows),int(groupsize)
cowl=[]
for prse in range(numcows):
    inp=int(fin.readline())
    cowl.append(inp)
mxval=[0]*numcows
mxval[0]=cowl[0]
for cur in range(numcows):
    possible=0
    #print(mxval)
    for pos in range(cur,-1,-1):
        precal=cur-pos+1
        if precal>groupsize:
            break
        possible=max(cowl[pos],possible)
        if pos==0:
            mxval[cur]=max(mxval[cur],possible*(precal))
        else:
            mxval[cur]=max(mxval[cur],mxval[pos-1]+possible*(precal))
fout.write(str(mxval[numcows-1]))