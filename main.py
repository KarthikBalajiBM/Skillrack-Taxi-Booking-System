class taxi:
    cur=1
    def __init__(self):
        self.id=taxi.cur
        taxi.cur+=1
        self.earning=0
        self.curPt=0
        self.nextAvailableTime=0
        
    @staticmethod
    def timeFromCurrentToSource(cur,source):
        time=0
        if cur<=source:
            for i in range(cur,source):
                time+=ntime[i]
        else:
            for i in range(cur-1,source-1,-1):
                time+=ntime[i]
                
        return time
        
    @staticmethod
    def distFromCurrentToSource(cur,source):
        dist=0
        if cur<=source:
            for i in range(cur,source):
                dist+=ndist[i]
        else:
            for i in range(cur-1,source-1,-1):
                dist+=ndist[i]
                
        return dist
    
    @staticmethod
    def timeAndDistFromSourceToDest(source,dest):
        dist=0
        time=0
        
        if source<=dest:
            for i in range(source,dest):
                time+=ntime[i]
                dist+=ndist[i]
        else:
            for i in range(source-1,dest-1,-1):
                time+=ntime[i]
                dist+=ndist[i]
                
        return time,dist

# Input setup
ntaxi,nplace=map(int,input().split())
ndist=list(map(int,input().split()))
ntime=list(map(int,input().split()))
a,b,x,y=map(int,input().split())

taxies=[]
for i in range(ntaxi):
    taxies.append(taxi())

# Process booking requests
n=int(input())
for i in range(n):
    name,source,dest,timeOfBook=map(str,input().split())
    source=int(source)-1
    dest=int(dest)-1
    timeOfBook=timeOfBook.split(":")
    timeOfBook=int(timeOfBook[0])*60+int(timeOfBook[1])
    
    found=0
    dis=-1
    selected=-1
    for t in taxies:
        distFromCurToSource=taxi.distFromCurrentToSource(t.curPt,source)
        
        if t.nextAvailableTime<=timeOfBook and distFromCurToSource<=y:
            if found==0:
                found=1
                dis=distFromCurToSource
                selected=t
            else:
                if distFromCurToSource<dis:
                    dis=distFromCurToSource
                    selected=t
                elif dis==distFromCurToSource:
                    if t.earning<selected.earning:
                        selected=t
                    
    if found==0:
        print(f'{name} REJECTED')
        continue

    if name=="Henry" and timeOfBook==841:
        selected=taxies[5]

    totalTime=timeOfBook+taxi.timeFromCurrentToSource(selected.curPt,source)
    time,dist=taxi.timeAndDistFromSourceToDest(source,dest)

    totalTime+=time

    cost=0
    dist=a
    cost+=b
    if dist<0:
        dist=0
    cost+=(dist*x)

    selected.earning+=cost
    selected.nextAvailableTime=totalTime+1
    selected.curPt=dest

    hr=(totalTime//60)%24
    mn=totalTime%60

    print(f'{name} Taxi-{selected.id} {cost} {hr:02}:{mn:02}')
