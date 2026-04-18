# Matrix addition:

dim=4
r1=[1,2,3,4]
r2=[4,5,6,7]
r3=[7,8,9,14]
r4=[1,1,2,2]

s1=[1,2,1,2]
s2=[6,2,3,15]
s3=[4,2,1,45]
s4=[1,7,2,9]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)
A.append(r4)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)
B.append(s4)

print('Matrix A is:', A)
# Matrix A is: [[1,2,3,4],[4,5,6,7],[7,8,9,14],[1,1,2,2]]
print('Matrix B is:', B)
# Matrix B is: [[1,2,1,2],[6,2,3,15],[4,2,1,45],[1,7,2,9]]
# We need to add A and B
c=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(dim):
    for j in range(dim):
        c[i][j]=A[i][j]+B[i][j]
print('Matrix A+B is:', c)
# Matric A+B is: [[2,4,4,6],[10,7,9,22],[11,10,10,59],[2,8,4,11]]