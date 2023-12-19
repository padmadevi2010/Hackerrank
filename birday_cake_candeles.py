a=int(input())
arr=list(map(int, input(). split()))
big=max(arr)
count=0
for i in range(len(arr)):
    if arr[i]==big:
       count += 1
print(count)            
  
  


