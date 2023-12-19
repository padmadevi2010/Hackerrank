a = list(map(int, input(). split()))
a=sorted(a)
minimum = sum(a[:-1])
maximum = sum(a[1:])
print(minimum, maximum)


