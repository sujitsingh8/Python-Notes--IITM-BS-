# Matrix Multiplication:

# c[i][j] is the dot product of ith row of a and jth column of b
r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

a=[]
a.append(r1)
a.append(r2)
a.append(r3)

b=[]
b.append(s1)
b.append(s2)
b.append(s3)

c=[[0,0,0],[0,0,0],[0,0,0]]

dim=3
# c[2][1] is the dot product of the 3rd row of a and the 2nd column of b
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
print(c)
# [[25,12,10],[58,30,25],[91,48,40]]