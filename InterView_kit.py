def sockMerchant(n, ar):
    # Write your code here
    ar=sorted(ar)
    fn=ar[0]
    pair=0
    flag=1
    for i in range(1,n):
        if ar[i]==fn and flag%2==1:
            pair=pair+1
            fn=ar[i]
            flag=flag+1
        else:
            if(flag%2==1):
                fn=ar[i]
                continue
            else:
                fn=ar[i]
                flag=flag+1
    return pair
    
def countingValleys(steps, path):
    # Write your code here
    down=0
    up=0
    count=0
    index=0
    for i in range(steps):
        if(path[i]=='D'):
            down=down+1
        elif(path[i]=='U'):
            up=up+1
        if(down==up and down!=0 and up!=0):
            index=down+up
            if (path[i-index+1]=='D'):
                count=count+1
                down=0
                up=0
            else:
                down=0
                up=0            
    return count
    
def jumpingOnClouds(c):
    # Write your code here
    n=len(c)
    i=0
    count=0
    while(i<n):
        if(i+2<n and c[i+2]==0):
            i=i+2
            count=count+1
            continue
        elif(i+1<n and c[i+1]==0):
            i=i+1
            count=count+1
            continue
        else:
            break
    return count

def hourglassSum(arr):
    # Write your code here
    rows, cols = (4, 4)
    arr1 = [[0 for i in range(cols)] for j in range(rows)]
    i=0
    j=1
    k=2
    r=0
    c=0
    while(r<4):
        while(c<4):
            arr1[r][c]=arr[r][i]+arr[r][j]+arr[r][k]+arr[r+1][c+1]+arr[r+2][i]+arr[r+2][j]+arr[r+2][k]
            c=c+1
            i+=1
            j+=1
            k+=1
        r=r+1
        i=0
        j=1
        k=2
        c=0
    return max([max(arr1[0][:]),max(arr1[1][:]),max(arr1[2][:]),max(arr1[3][:])])
    
def rotLeft(a, d):
    # Write your code here
    return a[d:] +a[:d]
    
def minimumBribes(q):
    # Write your code here
    n=len(q)
    i=1
    count=0
    temp=0
    flag=0
    k=q
    for i in range(n):
        if(q[i]>i+3):
            print("Too chaotic")
            return
    while(flag==0):
        for i in range(n-1):
            if(q[i]>q[i+1]):
                temp=q[i+1]
                q[i+1]=q[i]
                q[i]=temp
                count=count+1         
        if(sorted(k)==q):
            break        
    print(count)
    
def minimumSwaps(arr):
    # Write your code here
    count=0
    k={}
    for i in range(len(arr)-1):
        if(arr[i]==i+1):
            continue
        while(arr[i]!=i+1):
            if(arr[arr[i]-1]==i+1):
                arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
                count=count+1
                continue
            else:
                arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
                count=count+1
                
    return(count)
    
def arrayManipulation(n, queries):
    # Write your code here
    k=0
    arr=[ 0 for i in range(n + 1)]
    for i in range(len(queries)):
        low=queries[i][0]
        high=queries[i][1]
        k=queries[i][2]
        
        arr[low-1]+=k
        arr[high]-=k
        
    summ=0
    k=0
    
    for i in range(n):
        summ+=arr[i]
        if summ>k:
            k=summ
    return (k)
    
def checkMagazine(magazine, note):
    noted={}
    magazined={}
    for i in note:
        if i in noted:
            noted[i]=noted[i]+1
        else:
            noted[i]=1
    for j in magazine:
        if j in magazined:
            magazined[j]=magazined[j]+1
        else:
            magazined[j]=1
    
    for i in noted:
        if i not in magazined:
            print("No")
            return
        elif noted[i]>magazined[i]:
            print("No")
            return
    print("Yes") 
    
#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
    
def twoStrings(s1, s2):
    # Write your code here
    for i in s1:
        if i in s2:
            return("YES")
    return("NO") 
    
def freqQuery(queries):
    mp=dict()
    arr=[]
    for i in queries:
        if(i[0]==1):
            if i[1] in mp:
                mp[i[1]]+=1
            else:
                mp[i[1]]=1
        elif(i[0]==2):
            if i[1] not in mp or mp[i[1]]==0:
                continue
            else:
                mp[i[1]]=mp[i[1]]-1
        else:
            if i[1] in set(mp.values()):
                arr.append(1) 
            else:
                arr.append(0)
    return arr

def sherlockAndAnagrams(s):
    # Write your code here
    n=len(s)
    st=list(s)
    
    mp=dict()
    
    for i in range(n):
        sub=""
        for j in range(i,n):
            sub="".join(sorted(sub+s[j]))
            mp[sub] =mp.get(sub,0)
            mp[sub]+=1
                
        
    count=0
    
    for i,j in mp.items():
        count +=(j*(j-1))//2
    return count

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name=name
        self.score=score

    def comparator(a, b):
        if(a.score<b.score):
            return 1
        if(a.score==b.score and a.name==b.name):
            return 0
        if(a.score==b.score and a.name>b.name):
            return 1
        return(-1)
        

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)    
    
    
# Complete the countTriplets function below.
def countTriplets(arr, r):
    count=0
    ht={}
    ht1={}
    n=len(arr)
    for i in arr:
        ht1[i]=0
        if i in ht:
            ht[i]=ht[i]+1
        else:
            ht[i]=1
    if (r==1):
        for i in ht:
            if(ht[i]>=3):
                count=count+(math.factorial(ht[i])//(math.factorial(3)*math.factorial(ht[i]-3)))
        return count
            
    for i in range(n):
        ht1[arr[i]]+=1
        if arr[i]//r in ht1 and arr[i]*r in ht and arr[i]%r==0 :
            count=count + ((ht[arr[i]*r]-ht1[arr[i]*r])*(ht1[arr[i]//r]))
    return count
    
def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater
        
def countInversions(arr):
    # Write your code here
    base=sorted(arr)
    n=len(arr)
    i=0
    count=0
    while(base!=arr):
        if(arr[i]>arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            count+=1
        if(i==n-2):
            i=0
        else:
            i+=1
    return count
    
def countInversions(arr):
    # Write your code here
    n=len(arr)
    i=0
    j=0
    count=0
    
    while(i<n-1):
        if(arr[i]>arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            count+=1
            for j in range(i,0,-1):
                if(arr[j]<arr[j-1]):
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                    count+=1              
        else:
            i+=1
    #while(base!=arr):
    #    if(arr[i]>arr[i+1]):
    #        arr[i],arr[i+1]=arr[i+1],arr[i]
    #        count+=1
    #    if(i==n-2):
    #        i=0
    #    else:
    #        i+=1
    return count
    
def makeAnagram(a, b):
    # Write your code here
    ht=dict()
    ht1=dict()
    
    for i in a:
        ht[i]=ht.get(i,0)
        ht[i]+=1
    for i in b:
        ht1[i]=ht1.get(i,0)
        ht1[i]+=1
        
    count =0
    
    for i in ht:
        if i in ht1 and ht[i]>=ht1[i]:
            count+=ht[i]-ht1[i]
        elif i in ht1 and ht[i]<ht1[i]:
            count+=ht1[i]-ht[i]
        elif i not in ht1:
            count+=ht[i]
    for i in ht1:
        if i not in ht:
            count+=ht1[i]
    return count   

def alternatingCharacters(s):
    # Write your code here
    n=len(s)
    count=0
    for i in range(n-1):
        if s[i+1]==s[i]:
            count+=1
    return count    
    
    
def isValid(s):
    # Write your code here
    ht=dict()
    ht1=dict()
    for i in s:
        ht[i]=ht.get(i,0)
        ht[i]+=1
    arr=set(ht.values())
    ar=list(arr)
    arrr=list(ht.values())
    #return(str(arr))
    n=len(arr)
    if(n==1):                 
        return ("YES")
    if(n>2):
        return("NO")
    if(n==2):
        if(ar[0]-ar[1]==1 or ar[1]-ar[0]==1):
            if(arrr.count(ar[0])>1 and arrr.count(ar[1])>1):
                return("NO")
            else:
                return ("YES")
        if(ar[0]==1):            
            if(arrr.count(ar[0])>1):
                return("NO")
            return ("YES")
        if(ar[1]==1):            
            if(arrr.count(ar[1])>1):
                return("NO")
            return ("YES")        
    return("NO")
    
 def getMinimumCost(k, c):
    arr=sorted(c)
    arr.reverse()
    n=len(arr)
    pre=0
    j=1
    a=[]
    for i in range(n):
        a.append(arr[i]*(pre+1))
        if(j==k):
            pre+=1
            j=0
        j+=1
    return sum(a)
    
 def minimumAbsoluteDifference(arr):
    # Write your code here
    res=abs(arr[0]-arr[1])
    #arr = list(combinations(arr, 2))
    if len(arr) != len(list(set(arr))):
        return(0)
    arr=list(sorted(set(arr)))
    
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])<res:
            res=abs(arr[i]-arr[i+1])
    
    return res
    
def luckBalance(k, contests):
    # Write your code here
    arr=[]
    summ=0
    
    for i in contests:
        summ+=i[0]
        if(i[1]==1):
            arr.append(i[0])
    
    arr=sorted(arr)
    n=len(arr)
    su=0
    for i in range(n-k):
        su+=2*arr[i]
    
    return(summ-su)
    
def maxMin(k, arr):
    # Write your code here
    #return(len(ar))
    arr=sorted(arr)
    n=len(arr)
    le=1000000000000000
    for i in range(n-k+1):
        if arr[i+k-1]-arr[i]<le:
            le = arr[i+k-1]-arr[i] 
    return le

def whatFlavors(cost, money):
    # Write your code here
    ht={}
    for x,i in enumerate(cost):
        ht[i]=ht.get(i,[])
        ht[i].append(x)
        
    for i in ht:
            if(money-i == i):
                try:
                    print(ht[i][0]+1,ht[i][1]+1)
                    break
                except:
                    continue
            if(money-i in ht):
                #print(i,money-i)
                print(ht[i][0]+1,ht[money-i][0]+1)
                break
                
def minTime(machines, goal):
    ht=dict()
    machines=sorted(machines)
    for i in machines:
        ht[i]=ht.get(i,0)
        ht[i]+=1    
    n=goal
    count=0
    j=1
    machines=sorted(set(machines))
    while(True):
        for i in machines:
            if(j%i==0):
                count+=ht[i]
                if(count>=n):
                    return(j)
            elif(j<i):
                break
            elif(i>j):
                break
            else:
                continue
        j+=1
