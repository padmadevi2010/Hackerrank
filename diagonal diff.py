def d_diff(c):
    s=0
    t=0
    for i in range(len(c)):
        s=s+c[i][i]
    for j in range(len(c)):
        t=t+c[j][len(c)-1-j]
    diff=s-t
    return diff
a=int(input())
b=[]
for i in range(a):
    b.append(list(map(int, input(). split())))
result=d_diff(b)
print(abs(result))
