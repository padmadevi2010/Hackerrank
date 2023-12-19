a=int(input())
arr=list(map(int,input().split()))
s=0
t=0
u=0
for i in range(len(arr)):
    if arr[i]>0:
       s+=1
    elif arr[i]==0:
         t+=1
    elif arr[i]<0:
         u+=1
p=s/a
z=t/a
n=u/a
print(f"{p:.6f}")
print(f"{n:.6f}")  
print(f"{z:.6f}")       


