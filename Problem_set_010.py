a=input("Enter vowels = ")
vowels="aeoiu"
count=0
for ch in a:
    if ch in vowels:
        count=count+1
print(count)
