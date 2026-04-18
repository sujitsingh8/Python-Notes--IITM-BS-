# Birthday Paradox:

import random as ran
# if we take a group of people there will be at least two persons with the same birthday
l=[] # create an empty list

for i in range(50):
    l.append(ran.randint(1,365))
    # append random numbers between 1 to 365
    # append 50 of them
    # if born on jan 1st, the number is 1
    # if born on dec 31st, the number is 365
l.sort()
print(l)
i=0
flag=0
while(i<len(l)-1):
    if(l[i]==l[i+1]):
        print('repeats', l[i],l[i+1])
        flag=1
        break
    i+=1
if(flag==0):
    print('does not repests')
    
# as we increase the no. of people(range()) more accurate the birthday paradox will be!