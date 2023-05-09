count=0

s="this is a string"
al = set("aeiouAEIOU")

for alphabet in s:
    if alphabet in al:
        count=count+1
        
print(count)