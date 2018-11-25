'''
Currency used: 1, 2, 5, 10 kr coins and 20, 50, 100, 200, 500, 1000 kr bills
Reference for valid coins and banknotes:
https://www.riksbank.se/en-gb/payments--cash/notes--coins/notes/valid-banknotes/
https://www.riksbank.se/en-gb/payments--cash/notes--coins/coins/valid-coins/
'''
import sys

def get_change(cost, amount_paid):
    '''
    Returns the minimum number of coins and/or bills to make change.
    '''
    change = amount_paid - cost
    bill_counter = 0
    coin_counter = 0

    if change >= 1000:
        bill_counter += change // 1000
        change = change % 1000
    
    if change >= 500 and change < 1000:
        bill_counter += change // 500
        change = change % 500
    
    if change >= 200 and change < 500:
        bill_counter += change // 200
        change = change % 200
    
    if change >= 100 and change < 200:
        bill_counter += change // 100
        change = change % 100
    
    if change >= 50 and change < 100:
        bill_counter += change // 50
        change = change % 50

    if change >= 20 and change < 50:
        bill_counter += change // 20
        change = change % 20
    
    if change >= 10:
        coin_counter += change // 10
        change = change % 10

    if change >= 5 and change < 10:
        coin_counter += change // 5
        change = change % 5

    if change >= 2 and change < 5:
        coin_counter += change // 2
        change = change % 2

    if change >= 1 and change < 2:
        coin_counter += change // 1
    
    return '{0} coin(s) and {1} bill(s)'.format(coin_counter, bill_counter)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python change1.py <cost amount> <paid amount>')
    elif sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
        print('Decimal is not allowed.')
    else:
        print(get_change(int(sys.argv[1]), int(sys.argv[2])))