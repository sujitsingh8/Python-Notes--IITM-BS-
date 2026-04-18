# Writing the code for printing the table of the entered number

n=int(input('Enter a number: '))
for i in range(1,11):
    print(n,'X',i,'=',n*i)