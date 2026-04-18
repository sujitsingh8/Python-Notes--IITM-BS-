# Formatted printing:

# printinf numbers 0-9 in the same line in for loop - end parameter

for x in range(10):
    print(x,end=' ')
# 0 1 2 3 4 5 6 7 8 9

# (end) is used to print in the same line.
# The default value of the end parameter of print is \n(new line) but in this case we are telling the
# computer to override the default value and consider the ‘space’ as a new value.
# Now, while iterating it will print x and add space