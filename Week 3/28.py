# Find the total profit/loss for each trader in the trading firm

emp_id = input('\nEnter the employee Id: ')
while emp_id != '0':
    trade = int(input('Enter the trade amount: '))
    profit_loss= 0
    while trade!=0:
        profit_loss += trade
        trade = int(input('Enter the trade amount: '))
    print(f'Profit/loss for employee {emp_id} is {profit_loss}')
    emp_id = input('\nEnter employee Id: ')