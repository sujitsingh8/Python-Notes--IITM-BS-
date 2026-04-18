#  Find the number of digits in the given number

# Here we don't know how many times the loop is going to execute.
# The digit can have n number of digits so it is not possible to convert it into a for loop.

# But we can use ‘for each’.

num=abs(int(input('Enter a number: ')))
strnum=str(num)
digits=0
for c in strnum:
    digits+=1 # for every character in c in strnum do : digits +=1
print(digits)