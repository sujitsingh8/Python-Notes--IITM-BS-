# Let user search a particular element in the list

l=[2001,1999,1981,1985,2003,1988,1999]
n=0
while(n>-1):
    print('Enter a number, type -1 to exit:')
    n=int(input())
    flag=0
    for i in range (len(l)):
        if(n==l[i]):
            print('Element found')
            flag=1
            break
    if(flag==0):
            print('Element not found')