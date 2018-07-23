num=int(input('Enter a number'))
rev=0
temp=num
while num>0:
    rem=num%1000
    rev=rev*1000+rem
    num=num/1000
if rev==temp:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
