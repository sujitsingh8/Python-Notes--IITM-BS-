# Naive search in a list:

l=[1,2,3,48,9,7]
a=48

flag=0

for i in range(len(l)):
    if a==l[i]:
        print('element found')
        flag=1
        break
if flag==0:
    print('element not found')
    # element found