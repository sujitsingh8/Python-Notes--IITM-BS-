# Coding a quix program:

print('When did India get its Independence (Year)?: ')
year=int(input())

if year == 1947:
    print('Hip Hip Hurray, You got that right!')
else:
    print('Comeon don\'t ypu even know this?')
    print('That\'s okay, You can attempt this once again')
    print('When did India get its Independence (Year)?: ')
    year = int(input())
    if year == 1947:
        print('You got it')
    else:
        print('You failed in your second attempt too!')