# Computing Factorial of a Number:

n=int(input('Enter a Number: '))
i=1
answer=1
while(i<=n):
    answer=answer*i
    i=i+1
print(answer)

# n=5 (This is the input)

# i=1 (i<n i.e 1<5)
# answer = 1 (answer = answer *1, answer = 1*1)

# i=2 (2<5)
# answer = 2 (1*2)

# i=3 (3<5)
# answer = 6 (2*6)

# i = 4 (4<5)
# answer = 24 (6*4)

# i = 5 (5<=5)
# answer =120 (24*5)

# i=6 (6 is not less than 5)
# So, line 11 will execute