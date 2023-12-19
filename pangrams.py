def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    for char in alphabet:
        if char in str:
            return True
    return False
a= input().lower()
if(ispangram(a) == True):
    print("pangram")
else:
    print("not pangram")
