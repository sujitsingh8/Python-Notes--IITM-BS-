# format():

num=int(input('Enter a number: '))
for i in range(1,11):
    print('{0} X {1} = {2}'.format(num,i,num*i))

# Before it was like:

# for i in range (1,11):
    # print('2 X', i, '=',2*i)
    
# num=int(input('Enter a number: '))
# for i in range(1,11):
#     print(f'{num} X {i} = {num*i}')

# There are three pairs of curly braces. The values that go into these three positions are
# given as three arguments in the ‘format function’. Starting from the left, the first pair of
# curly braces in the string is replaced by the first argument in ‘format’ ,  the second pair
# by the second argument and so on.

# The integer inside the curly braces gives the index of the argument in the format
# function. The arguments of the format function are indexed from 0 and start from the
# left. Changing the order of arguments will change the output.