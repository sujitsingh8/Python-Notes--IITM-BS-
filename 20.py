# Format specifiers:

pi=22/7
print(f'The value of Pi = {pi}')
print('The value of Pi = {0}'.format(pi))
print('The value of Pi = %f' % (pi)) # %f = float, this is very old method of creating formatted strings

# The value of Pi = 3.142857142857143
# The value of Pi = 3.142857142857143
# The value of Pi = 3.142857

# What if we wanr the answer up-to 2 decimals only?

pi=22/7
print(f'The value of Pi = {pi:.2f}') # only two digits after decimal
print('The value of Pi = {0:.2f}'.format(pi))
print('The value of Pi = %.2f' % (pi)) # %f = float

# Let us look at the content inside the curly braces: {pi:.2f}. 
# The first part before the : is the variable.
# Nothing new here. The part after : is called a format specifier.
 
# .2f means the following:
#   ● .-  this signifies the decimal point.
#   ● 2-  since this comes after the decimal point, it stipulates that there should be
#     exactly two numbers after the decimal point. In other words, the value (pi_approx)
#     should be rounded off to two decimal places.
#   ● f-  this signifies that we are dealing with a float value.

#...........................................................................................................

# For a better understanding of this concept, let us turn to printing integers with a specific
# formatting. This time, we will use the format function:

print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))

# Points to note in the code:
#   ● Thedstands for integer.
#   ● First three print statements have the index of the argument — 0 in this case —
#     before the :. Last three statements do not have the index of the argument. In fact
#     there is nothing before the :. Both representations are valid.
#   ● The5dafter the : means that the width of the column used for printing must be at least 5.
#   ● Lines 1 to 4 have spaces before them as the integer being printed has fewer than five characters.