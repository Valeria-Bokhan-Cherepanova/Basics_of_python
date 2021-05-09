profit = int(input('Enter profit: '))
expense = int(input('Enter expense: '))


if profit > expense:
    profitability = profit - expense
    print(f'The firm operates at a profit. The profitability is {profitability}')
    worker = int(input('How many people work: '))
    print(f'{profitability/worker} for one worker')


elif profit == expense:
    print('The firm operates at zero')
else:
    print('The firm operates at a loss:(')

