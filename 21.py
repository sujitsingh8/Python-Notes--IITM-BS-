# Tutorial on for loop and difference between while loop and for loop:

# Finf the factorial of the given number

num=int(input('Enter a number: '))
fact=1
if(num<0):
    print('Not defined')
else:
    for i in range(num,1,-1):
        fact=fact*i
    print(fact)

# What are the factors we should consider before deciding whether to use while loop or for loop?

# Do we know the range of the loop in advance or not?
# If yes we should use ‘for loop’.

# if we don't know how many times the particular loop is going to execute we should use
# ‘while loop’.