# The obvious sort:

l=[1,6,89,54,34,245]
l.sort() # sorts in ascending order
print(l)
# [1,6,34,54,89,245]

l.sort(reverse=True) # sorts in descending order
print(l)
# [245,89,54,34,6,1]

#...........................................................................................................

# Without using built in functions

l=[12,10,7,18,6,42,8,5]
x=[]
while(len(l)>0):
    min=l[0]
    for i in range(len(l)):
        if l[i]<min:
            min=l[i]
    x.append(min)
    l.remove(min)
print(l)
# []
print(x)
# [5,6,7,8,10,12,18,42]