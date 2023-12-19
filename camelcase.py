def camelcase(s):
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count
c_case = input()
result = camelcase(c_case)
print(result)
