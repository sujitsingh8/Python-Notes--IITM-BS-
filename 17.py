# Sep paramter

d=10
m=5
y=2021
print('Today\'s date is ',d,m,y,sep='/')
# today's date is /10/5/2021

# ‘sep parameter’ has a default value as a ‘space’ , we can override the value of sep parameter
# explicitly mentioning some value.
# Here, we mentioned (sep = '\')
# But here is a small error : slash between is and 10

print("today's date is")
print(d,m,y,sep='/')
# today's date is
# 10/5/2021

# But it's in next line, we want to print it in same line

print("today's date is ",end='')
print(d,m,y,sep='/')
# today's date is 10/5/2021