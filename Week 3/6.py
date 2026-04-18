# Reverse a number:

num=int(input('Enter a number: '))
absNum=abs(num)
rev=0
if num>=0:
    while(num>0):
        r=num%10 # take remainder
        num=num//10 # removes last digit each time
        rev=rev*10+r
    print(rev)
    
else:
    while(absNum>0):
        r=absNum%10
        absNum=absNum//10
        rev=rev*10+r
    print(rev-2*rev)  # it will substract the same number twice to reserve the negative sign