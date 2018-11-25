'''
Currency used: 1, 2, 5, 10 kr coins
Reference for valid coins:
https://www.riksbank.se/en-gb/payments--cash/notes--coins/coins/valid-coins/
'''

import sys

def get_change(cost, amount_paid):
    '''
    Returns the minimum number of coins to make change.
    '''
    change = amount_paid - cost
    coin_counter = 0
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
    return coin_counter

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python change0.py <cost amount> <paid amount>')
    elif sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
        print('Decimal is not allowed.')
    else:
        print(get_change(int(sys.argv[1]), int(sys.argv[2])))