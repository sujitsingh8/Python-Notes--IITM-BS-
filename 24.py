# Find whether the digit is a palindrome or not

num=int(input('Enter a number: '))
absstrnum=str(abs(num))
rev=''

for c in absstrnum:
    rev=c+rev
if(num<0):
    rev='-'+rev
if(num==int(rev)):
    print('Palindrome')
else:
    print('Not Palindrome')
    
    
# Most convenient way of using loops for different questions:

# 1. Find the factorial of the guven number - for
# 2. Find the number of digits in the given number - while
# 3. Reverse the digits in the given number - while
# 4. Find whether the entered number is palindrome or not - while
# 5. Accept integrs using input() function to find max until the input is -1 - while
# 6. Print the multiplication table of the given number - for
# 7. Find whether the given number is prime or not - for
# 8. Find the sum of all digits in the given number - while
# 9. Find all factors of the given number - for