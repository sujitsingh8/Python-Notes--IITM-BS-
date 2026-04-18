# Find the day wise total rainfall for the entered duration of time eg week month,etc

days = int(input('Enter the number of days: '))
for i in range(1,days+1):
    total = 0
    rainfall=int(input('Enter rainfall (1 to count or -1 to stop): '))
    while rainfall != -1:
        total = total +1
        rainfall = int(input('Enter rainfall (1 to count or -1 to stop): '))
    print('Total rainfall for day {0} is {1}' .format(i,total))