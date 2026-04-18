# Nested for loop:

# There are two brothers who wear t-shirts of either of the colors in VIB(Violet, Indigo,
# Blue)  . Can we tell what are the possible combinations they can wear.

s='VIB'
t='VIB'
count=0
for i in range(3):
    for j in range(3):
        print(i,j,s[i],s[j])
        count+=1
print('They can wear in', count, 'ways')

# Brief explanation
# i=0 and j=0 print vv
# i=0 and j=1 print vi
# i=0 and j=2 print vb
# i=1 and j=0 print iv
# and so on......abs

# Output:
# 0 0 V V
# 0 1 V I
# 0 2 V B
# 1 0 I V
# 1 1 I I
# 1 2 I B
# 2 0 B V
# 2 1 B I
# 2 2 B B
# They can wear in 9 ways