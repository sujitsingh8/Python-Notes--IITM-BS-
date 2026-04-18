# Understanding more about for loop:

n=int(input('Enter a number: ')) 
for i in range (1,n+1): # the variable i will take the values from the range 1 to n+1
    if(i%2==0):
        print(i,'hey') # it will be excuted if it passes the condition in if statement
    else:
        print(i,'hi')
        
# this code prints 'hi' for off number and 'hey' for even numbers