# Find the number of digits in the given number:

num=abs(int(input('Enter a number: '))) # The abs() function returns the absolute value of the specified number.
# It wull take input from the user and store it as a integer and 
# then it will convert the integer to its absolute value.

digits=1 # it covers all numbers from -9 to 9

while(num>9):
    num=num//10 # if the number is 1234 it will reduce it to as 123 and 
    # if we keep doing this it will keep on reducing it further as 12 and then to 1
    digits=digits+1
print(digits)