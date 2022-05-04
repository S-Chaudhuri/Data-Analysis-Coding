a = input("Enter word= ")
Flag = True
for i in range(0,int(len(a)/2)):
    if a[i] != a[len(a)-i-1]:
        Flag = False
if Flag:
    print("Is a Palindrome")
else:
    print("Not a Palindrome")