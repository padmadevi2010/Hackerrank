def share_common_substring(str1, str2):
    for char in str1:
        if char in str2:
            return True
    return False
string1 = input()
string2 = input()
if share_common_substring(string1, string2):
    print("Yes")
else:
    print("No")

