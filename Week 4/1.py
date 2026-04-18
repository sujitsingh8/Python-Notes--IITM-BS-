# Warmup with lists:

l=[1,2,3]
print(l)
# [1,2,3]

l.append(9) # adds the element in the list
print(l)
# [1,2,3,9]

l.append(2)
print(l) # it repeats the element its not like sets
# [1,2,3,9,2]

l.remove(1) # it removes 1 from the lsit
print(l) 
# [2,3,9,2]

l.remove(2) # it will remove the first occurence of 2
print(l)
[3,9,2]

#...........................................................................................................

x=[]
m=[1,2,3]
n=[4,5,6]
x.append(m)
x.append(n)
print(x) # lists within a list
# [[1,2,3],[4,5,6]]

#...........................................................................................................

t=[]
t.append(x)
print(t) # it is a list containing list containing 2 lists
# [[[1,2,3],[4,5,6]]]

t.append([7,8,9])
print(t)
# [[[1,2,3],[4,5,6]],[7,8,9]]

#...........................................................................................................

print(t)
# [[[1,2,3],[4,5,6]],[7,8,9]]

print('list t is of length', len(t))
# length t is of length 2

print('first element of list t is',t[0])
# first element of list t is [[1,2,3],[4,5,6]]

print(t[0][0])
# [1,2,3]

print(t[0][0][0])
# 1

#...........................................................................................................

M=[]
M.append([1,2,3])
M.append([4,5,6])
M.append([7,8,9])

print(M) # it is a 3*3 matrix
# [[1,2,3],[4,5,6],[7,8,9]]

print(M[0][0])
# 1

print(M[1][1])
# 5

print(M[2][2])
# 9