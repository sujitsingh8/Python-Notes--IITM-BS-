# Codes of tutorials on nested loops :


# Find all prime numbers less than the entered number 

num = int(input('Enter a number: '))
if(num>2):
    print(2,end=' ')
for i in range (3,num): # This loop checks each number i starting from 3 up to num-1
    flag = False
    for j in range(2,i): # This checks if i is divisible by any number from 2 to i-1.
        if(i%j==0):
            flag = False
            break
        else:
            flag =True
    if(flag):
        print(i,end=' ')