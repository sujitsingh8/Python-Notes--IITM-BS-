# Find whether the entered number is a palindrome ir not:

num=int(input('Enter a number: '))
absNum=n=abs(num)
m=num
rev=0
if num>=0:
    while(num>0):
        r=num%10
        num=num//10
        rev=rev*10+r
    if(rev==n):
        print('The number is a palindrome number.')
    else:
        print('The number is not a palindrome number.')
    
else:
    while(absNum>0):
        r=absNum%10
        absNum=absNum//10
        rev=rev*10+r
    if(m==(rev-2*rev)):
        print('The number is a palindrome number.')
    else:
        print('The number is not a palindrome number.')