s=input().upper()
signal="SOS"
count=0
for i in range(len(s)):
    if(s[i]!=signal[i%3]):
        count+=1
print(count)