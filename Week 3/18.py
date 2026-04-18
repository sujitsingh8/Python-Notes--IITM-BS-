# F-string

num=int(input('Enter a number: '))
for i in range(1,11):
    print(f'{num} X {i} = {num*i}')

# Before it was like:

# for i in range (1,11):
    # print('2 X', i, '=',2*i)
    
# The ‘f’ in front of the string differentiates f-strings from normal strings.
# f-string is an object which when evaluated results in a string. The value of the variable num, i and
# num*i is inserted in place of {num} {i} {num*i} in the f-string. 

# Two things are important for f-strings to do our bidding:
#   ● The f in front of the string.
#   ● The curly braces enclosing the variable.