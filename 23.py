# Reverse a number

num=int(input('Enter a number: '))
absstrum = str(abs(num))
rev=''
for c in absstrum:
    rev=c+rev
if(num>=0):
    print(rev)
else:
    print('-'+rev) # in order to reverse -negative sign