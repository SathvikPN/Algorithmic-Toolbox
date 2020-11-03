# Uses python3
import sys
from math import lcm

def get_change(m): #m==money
    #write your code here
    LCM = lcm(1,3,4) #LCM of denominations available
    ''' Safe whole number and it's least coins is with biggest denomination'''
    safeCoins = (m//LCM)*3
    print(f'safeCoins {safeCoins} of [Rs.4]')
    remaining = m%LCM #remaining < LCM
    print('FillingCoins')
    coins = [0,0]
    for i in [0,1]:
        r = remaining
        if i==0:
            add4 = r//4
            rem = r%4
            add3 = rem//3 if rem%3==0 else 0
            add1 = rem%3
            coins[i] = add4+add3+add1
            print(f'<1> {add4}[Rs.4] + {add3}[Rs.3] + {add1}[Rs.1] = {coins[i]} Coins')
        else:
            add3 = r//3
            add1 = r%3
            add4 = 0
            while add1>0 and add3>0:
                for j in range(1,add1+1):
                    add4 = add4 + 1
                    add3 = add3 - 1
                    add1 = add1 - 1
            coins[i] = add4 + add3 + add1
            print(f'<2> {add4}[Rs.4] + {add3}[Rs.3] + {add1}[Rs.1] = {coins[i]} Coins')
    print('Best Choice is Minimum of',coins)
    return safeCoins + min(coins)
    
if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
