# break, continue and pass:

# break:

email=input('Enter an email: ')
for c in email:
    if c=='@':
        break
    print(c,end='')
# Enter an email: sujitsingh8389@gmail.com
# sujitsingh8389
    
# The break statement is used to exit out of a loop without executing any code that comes below it.

#...........................................................................................................

# continue:

email=input('\nEnter an email: ')
for c in email:
    if c=='@':
        print('')
        continue # It skips one iteration in between and jumps to next value
    print(c,end='')
# Enter an email: sujitsingh8389@gmail.com
# sujitsingh8389
# gmail.com

# The continue statement is used to move to the next iteration of the loop, skipping  whatever code comes below it.

#...........................................................................................................

# pass:

# divisible by 3 and not divisible by 3

for x in range (11):
    if x%3==0:
        print(x)
    else:
        pass # it is like a null statement
# 0
# 3
# 6
# 9

# In Python, pass is a null statement. The interpreter does not ignore a pass statement,
# but nothing happens and the statement results in no operation